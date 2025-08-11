"""Platform-specific utility functions for browser automation."""

import ctypes
import os
import platform
import subprocess
import sys
from typing import List, Optional


def is_running_as_root() -> bool:
    """
    Check if the current process is running with elevated privileges.
    
    Returns:
        bool: True if running as root (Linux/macOS) or administrator (Windows)
    """
    system = platform.system().lower()
    
    if system in ('linux', 'darwin'):  # Linux or macOS
        try:
            return os.getuid() == 0
        except AttributeError:
            return False
    elif system == 'windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except (AttributeError, OSError):
            return False
    else:
        return False


def is_running_in_container() -> bool:
    """
    Check if the process is running inside a container (Docker, etc.).
    
    Returns:
        bool: True if likely running in a container
    """
    container_indicators = [
        os.path.exists('/.dockerenv'),
        os.path.exists('/proc/1/cgroup') and 'docker' in open('/proc/1/cgroup', 'r').read(),
        os.environ.get('container') is not None,
        os.environ.get('KUBERNETES_SERVICE_HOST') is not None,
    ]
    
    return any(container_indicators)


def get_required_sandbox_args() -> List[str]:
    """
    Get the required browser arguments for sandbox handling based on current environment.
    
    Returns:
        List[str]: List of browser arguments needed for current environment
    """
    args = []
    
    if is_running_as_root():
        args.extend([
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ])
    
    if is_running_in_container():
        args.extend([
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--single-process',
        ])
    
    seen = set()
    unique_args = []
    for arg in args:
        if arg not in seen:
            seen.add(arg)
            unique_args.append(arg)
    
    return unique_args


def merge_browser_args(user_args: Optional[List[str]] = None) -> List[str]:
    """
    Merge user-provided browser arguments with platform-specific required arguments.
    
    Args:
        user_args: User-provided browser arguments
        
    Returns:
        List[str]: Combined list of browser arguments
    """
    user_args = user_args or []
    required_args = get_required_sandbox_args()
    
    combined_args = list(user_args)
    
    for arg in required_args:
        if arg not in combined_args:
            combined_args.append(arg)
    
    return combined_args


def get_platform_info() -> dict:
    """
    Get comprehensive platform information for debugging.
    
    Returns:
        dict: Platform information including OS, architecture, privileges, etc.
    """
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'architecture': platform.architecture(),
        'python_version': sys.version,
        'is_root': is_running_as_root(),
        'is_container': is_running_in_container(),
        'required_sandbox_args': get_required_sandbox_args(),
        'user_id': getattr(os, 'getuid', lambda: 'N/A')(),
        'effective_user_id': getattr(os, 'geteuid', lambda: 'N/A')(),
        'environment_vars': {
            'DISPLAY': os.environ.get('DISPLAY'),
            'container': os.environ.get('container'),
            'KUBERNETES_SERVICE_HOST': os.environ.get('KUBERNETES_SERVICE_HOST'),
            'USER': os.environ.get('USER'),
            'USERNAME': os.environ.get('USERNAME'),
        }
    }


def check_chrome_executable() -> Optional[str]:
    """
    Find the Chrome/Chromium executable on the system.
    
    Returns:
        Optional[str]: Path to Chrome executable or None if not found
    """
    system = platform.system().lower()
    
    if system == 'windows':
        possible_paths = [
            r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            r'C:\Users\{}\AppData\Local\Google\Chrome\Application\chrome.exe'.format(os.environ.get('USERNAME', '')),
            r'C:\Program Files\Chromium\Application\chromium.exe',
        ]
    elif system == 'darwin':
        possible_paths = [
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            '/Applications/Chromium.app/Contents/MacOS/Chromium',
        ]
    else:
        possible_paths = [
            '/usr/bin/google-chrome',
            '/usr/bin/google-chrome-stable',
            '/usr/bin/chromium',
            '/usr/bin/chromium-browser',
            '/snap/bin/chromium',
            '/usr/local/bin/chrome',
        ]
    
    for path in possible_paths:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    
    chrome_names = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser', 'chrome']
    for name in chrome_names:
        try:
            result = subprocess.run(['which', name], capture_output=True, text=True)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (subprocess.SubprocessError, FileNotFoundError):
            continue
    
    return None


def validate_browser_environment() -> dict:
    """
    Validate the browser environment and return status information.
    
    Returns:
        dict: Environment validation results
    """
    chrome_path = check_chrome_executable()
    platform_info = get_platform_info()
    
    issues = []
    warnings = []
    
    if not chrome_path:
        issues.append("Chrome/Chromium executable not found")
    
    if platform_info['is_root']:
        warnings.append("Running as root/administrator - sandbox will be disabled")
    
    if platform_info['is_container']:
        warnings.append("Running in container - additional arguments will be added")
    
    if platform_info['system'] not in ['Windows', 'Linux', 'Darwin']:
        warnings.append(f"Untested platform: {platform_info['system']}")
    
    return {
        'chrome_executable': chrome_path,
        'platform_info': platform_info,
        'issues': issues,
        'warnings': warnings,
        'is_ready': len(issues) == 0,
        'recommended_args': get_required_sandbox_args(),
    }
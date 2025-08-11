# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and adheres to Semantic Versioning where practical.

## [0.2.4] - 2025-08-11
### Fixed
- **🛡️ Root User Browser Spawning** - Fixed "Failed to connect to browser" when running as root/administrator
- **📝 Args Parameter Validation** - Fixed "Input validation error" for JSON string args format
- **🐳 Container Environment Support** - Added Docker/Kubernetes compatibility with auto-detection
- **🔧 Cross-Platform Compatibility** - Enhanced Windows/Linux/macOS support with platform-aware configuration

### Added
- **🔍 `validate_browser_environment_tool()`** - New diagnostic tool for environment validation
- **⚙️ Smart Platform Detection** - Auto-detects root privileges, containers, and OS-specific requirements
- **🔄 Flexible Args Parsing** - Supports JSON arrays, JSON strings, and single string formats
- **📊 Enhanced Logging** - Added platform information to browser spawning debug logs
- **🛠️ `platform_utils.py`** - Comprehensive cross-platform utility module

### Enhanced
- **Browser Argument Handling** - Automatically merges user args with platform-required args
- **Environment Detection** - Detects root/administrator, container environments, and Chrome installation
- **Error Messages** - More descriptive error messages with platform-specific guidance
- **Sandbox Management** - Intelligent sandbox disabling based on environment detection

### Technical
- Added `merge_browser_args()` function for smart argument merging
- Added `is_running_as_root()` cross-platform privilege detection
- Added `is_running_in_container()` for Docker/Kubernetes detection
- Enhanced `spawn_browser()` with comprehensive args parsing
- Improved browser configuration with nodriver Config object
- Total tool count increased from 89 to 90 tools

## [0.2.3] - 2025-08-10
### Added
- **⚡ `paste_text()` function** - Lightning-fast text input via Chrome DevTools Protocol
- **📝 Enhanced `type_text()`** - Added `parse_newlines` parameter for proper Enter key handling
- **🚀 CDP-based text input** - Uses `insert_text()` method for instant large content pasting
- **💡 Smart newline parsing** - Converts `\n` strings to actual Enter key presses when enabled

### Enhanced  
- **Text Input Performance** - `paste_text()` is 10x faster than character-by-character typing
- **Multi-line Form Support** - Proper handling of complex multi-line inputs and text areas
- **Content Management** - Handle large documents (README files, code blocks) without timeouts
- **Chat Application Support** - Send multi-line messages with preserved line breaks

### Technical
- Implemented `DOMHandler.paste_text()` using `cdp.input_.insert_text()` 
- Enhanced `DOMHandler.type_text()` with line-by-line processing for newlines
- Added proper fallback clearing methods for both functions
- Updated MCP server endpoints with new `paste_text` tool
- Updated tool count from 88 to 89 functions

## [0.2.2] - 2025-08-10
### Added
- **🎛️ Modular Tool System** - CLI arguments to disable specific tool sections
- **⚡ --minimal mode** - Run with only core browser management and element interaction tools
- **📋 --list-sections** - List all 11 tool sections with tool counts
- **🔧 Granular Control** - Individual disable flags for each of 11 tool sections:
  - `--disable-browser-management` (11 tools)
  - `--disable-element-interaction` (10 tools) 
  - `--disable-element-extraction` (9 tools)
  - `--disable-file-extraction` (9 tools)
  - `--disable-network-debugging` (5 tools)
  - `--disable-cdp-functions` (13 tools)
  - `--disable-progressive-cloning` (10 tools)
  - `--disable-cookies-storage` (3 tools)
  - `--disable-tabs` (5 tools)
  - `--disable-debugging` (6 tools)
  - `--disable-dynamic-hooks` (10 tools)
- **🏗️ Clean Architecture** - Section-based decorator system for conditional tool registration

### Changed
- Updated CLI help text to show "88 tools" and new section options
- Reorganized tool registration using `@section_tool()` decorator pattern
- All tools now conditionally register based on disabled sections set

### Technical
- Implemented `DISABLED_SECTIONS` global set for tracking disabled functionality
- Added `is_section_enabled()` helper function
- Created `@section_tool("section-name")` decorator for conditional registration
- Tools are only registered if their section is enabled

## [0.2.1] - 2025-08-09
### Added
- **🚀 Dynamic Network Hook System** - AI-powered request/response interception
- **🧠 AI Hook Learning System** - 10 comprehensive hook examples and documentation
- **⚡ Real-time Processing** - No pending state, immediate hook execution
- **🐍 Custom Python Functions** - AI writes hook logic with full syntax validation
- **🔧 Hook Management Tools** - Create, list, validate, and remove hooks dynamically

### Fixed
- RequestId type conversion issues in CDP calls
- Missing imports in hook learning system
- Syntax errors in browser manager integration
- **Smithery.ai deployment Docker build failure** - Added `git` to Dockerfile system dependencies for py2js installation
- **Smithery.ai PORT environment variable support** - Server now reads PORT env var as required by Smithery deployments
- **Docker health check endpoint** - Updated health check to use correct /mcp endpoint with dynamic PORT

### Changed
- Replaced old network hook system with dynamic architecture
- Updated documentation to reflect new capabilities
- **Removed 13 broken/incomplete network hook functions** - Moved to `oldstuff/old_funcs.py` for reference
- **Corrected MCP tool count to 88 functions** - Updated all documentation consistently

### Removed
- `create_request_hook`, `create_response_hook`, `create_redirect_hook`, `create_block_hook`, `create_custom_response_hook` - These functions were calling non-existent methods
- `list_network_hooks`, `get_network_hook_details`, `remove_network_hook`, `update_network_hook_status` - Management functions for the broken hook system
- `list_pending_requests`, `get_pending_request_details`, `modify_pending_request`, `execute_pending_request` - Pending request management (replaced by real-time dynamic hooks)

## [0.2.0] - 2025-08-08
### Added
- Initial dynamic network hook system implementation
- Real-time request/response processing architecture

## [0.1.0] - 2025-08-07
### Added
- Initial public README overhaul
- Community health files (CoC, Contributing, Security, Roadmap, Changelog)
- Issue and PR templates



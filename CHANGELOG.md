# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and adheres to Semantic Versioning where practical.

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



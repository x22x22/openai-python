#!/usr/bin/env python3
"""Example: Discovering available tools for the Responses API.

This example demonstrates how to use the tool discovery functions to find out
what tools are available for use with the /v1/responses endpoint.
"""

from openai import get_tool_info, get_all_tools_info, get_available_tool_types

# Example 1: Get a list of all available tool types
print("=" * 80)
print("Example 1: List all available tool types")
print("=" * 80)
tool_types = get_available_tool_types()
print(f"\nAvailable tool types ({len(tool_types)}):")
for tool_type in tool_types:
    print(f"  - {tool_type}")

# Example 2: Get detailed information about a specific tool
print("\n" + "=" * 80)
print("Example 2: Get information about the 'web_search' tool")
print("=" * 80)
web_search_info = get_tool_info("web_search")
print(f"\nTool type: web_search")
print(f"Description: {web_search_info['description']}")
print(f"Documentation: {web_search_info['documentation_url']}")
print(f"Required parameters: {', '.join(web_search_info['required_params'])}")
print(f"Optional parameters: {', '.join(web_search_info['optional_params'])}")

# Example 3: Get information about MCP tools
print("\n" + "=" * 80)
print("Example 3: Get information about the 'mcp' tool")
print("=" * 80)
mcp_info = get_tool_info("mcp")
print(f"\nTool type: mcp")
print(f"Description: {mcp_info['description']}")
print(f"Documentation: {mcp_info['documentation_url']}")
print(f"Required parameters: {', '.join(mcp_info['required_params'])}")
print(f"Optional parameters:")
for param in mcp_info["optional_params"]:
    print(f"  - {param}")

# Example 4: Get information about code_interpreter
print("\n" + "=" * 80)
print("Example 4: Get information about the 'code_interpreter' tool")
print("=" * 80)
code_interpreter_info = get_tool_info("code_interpreter")
print(f"\nTool type: code_interpreter")
print(f"Description: {code_interpreter_info['description']}")
print(f"Documentation: {code_interpreter_info['documentation_url']}")

# Example 5: Get information about all tools at once
print("\n" + "=" * 80)
print("Example 5: Get information about all tools")
print("=" * 80)
all_tools = get_all_tools_info()
print(f"\nTotal tools available: {len(all_tools)}\n")
for tool_type, info in all_tools.items():
    print(f"{tool_type}:")
    print(f"  {info['description']}")
    print()

# Example 6: Filter tools by category
print("=" * 80)
print("Example 6: Categorize tools")
print("=" * 80)

built_in_tools = ["web_search", "file_search", "code_interpreter", "image_generation"]
custom_tools = ["function", "custom", "function_shell"]
mcp_tools = ["mcp"]
advanced_tools = ["computer", "local_shell", "apply_patch"]

print("\nBuilt-in Tools (provided by OpenAI):")
for tool in built_in_tools:
    if tool in tool_types:
        print(f"  - {tool}: {get_tool_info(tool)['description'][:60]}...")

print("\nCustom Tools (defined by you):")
for tool in custom_tools:
    if tool in tool_types:
        print(f"  - {tool}: {get_tool_info(tool)['description'][:60]}...")

print("\nMCP Tools (third-party integrations):")
for tool in mcp_tools:
    if tool in tool_types:
        print(f"  - {tool}: {get_tool_info(tool)['description'][:60]}...")

print("\nAdvanced Tools:")
for tool in advanced_tools:
    if tool in tool_types:
        print(f"  - {tool}: {get_tool_info(tool)['description'][:60]}...")

print("\n" + "=" * 80)
print("Tool discovery complete!")
print("=" * 80)

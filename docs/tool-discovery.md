# Tool Discovery for the Responses API

This guide explains how to use the tool discovery functions to learn about available tools for the `/v1/responses` endpoint.

## Overview

When using the OpenAI Responses API, you can enhance the model's capabilities by providing it with various tools. The tool discovery functions help you programmatically discover what tools are available and understand how to use them.

## Available Functions

### `get_available_tool_types()`

Returns a list of all available tool types that can be used with the Responses API.

```python
from openai import get_available_tool_types

tool_types = get_available_tool_types()
print(f"Available tools: {', '.join(tool_types)}")
```

**Output:**
```
Available tools: function, file_search, computer, web_search, mcp, code_interpreter, image_generation, local_shell, function_shell, custom, web_search_preview, apply_patch
```

### `get_tool_info(tool_type)`

Returns detailed information about a specific tool, including its description, documentation URL, and required/optional parameters.

```python
from openai import get_tool_info

web_search_info = get_tool_info("web_search")
print(f"Description: {web_search_info['description']}")
print(f"Documentation: {web_search_info['documentation_url']}")
print(f"Required params: {web_search_info['required_params']}")
print(f"Optional params: {web_search_info['optional_params']}")
```

**Output:**
```
Description: A built-in tool for searching the web to find current information.
Documentation: https://platform.openai.com/docs/guides/tools-web-search
Required params: ['type']
Optional params: ['filters', 'user_location']
```

### `get_all_tools_info()`

Returns a dictionary containing information about all available tools.

```python
from openai import get_all_tools_info

all_tools = get_all_tools_info()
for tool_type, info in all_tools.items():
    print(f"{tool_type}: {info['description'][:60]}...")
```

## Tool Categories

### Built-in Tools (Provided by OpenAI)

These tools are hosted and maintained by OpenAI:

- **`web_search`**: Search the web for current information
- **`file_search`**: Search through files and documents
- **`code_interpreter`**: Run Python code to help generate responses
- **`image_generation`**: Generate images using GPT image models

### Custom Tools (Defined by You)

These tools allow you to extend the model with your own functionality:

- **`function`**: Call your own functions with strongly typed arguments
- **`custom`**: Define custom tools with specific parameters
- **`function_shell`**: Execute shell-based function tools

### MCP Tools (Third-party Integrations)

- **`mcp`**: Model Context Protocol servers for third-party integrations

### Advanced Tools

- **`computer`**: Interact with a computer interface
- **`local_shell`**: Execute shell commands in a local environment
- **`apply_patch`**: Apply code patches to files
- **`web_search_preview`**: Preview version of web search with additional features

## Example Usage

Here's a complete example showing how to discover and use tools:

```python
from openai import OpenAI, get_available_tool_types, get_tool_info

client = OpenAI()

# Discover available tools
print("Discovering available tools...")
tool_types = get_available_tool_types()

# Get information about web_search
web_search_info = get_tool_info("web_search")
print(f"\nUsing tool: web_search")
print(f"Description: {web_search_info['description']}")

# Use the web_search tool in a response
response = client.responses.create(
    model="gpt-4o",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "web_search"}],
)

print(f"\nResponse: {response.output_text}")
```

## Checking Tool Requirements

Before using a tool, you can check its requirements:

```python
from openai import get_tool_info

# Check MCP tool requirements
mcp_info = get_tool_info("mcp")

print("MCP Tool Requirements:")
print(f"Required parameters: {', '.join(mcp_info['required_params'])}")
print(f"\nOptional parameters:")
for param in mcp_info['optional_params']:
    print(f"  - {param}")
```

## Error Handling

The `get_tool_info()` function raises a `ValueError` if you request information about an unknown tool:

```python
from openai import get_tool_info

try:
    info = get_tool_info("nonexistent_tool")
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Unknown tool type: nonexistent_tool. Available types: ...
```

## Complete Example

See the [tool_discovery.py](../examples/tool_discovery.py) example for a comprehensive demonstration of all tool discovery features.

## API Reference

### Return Types

All functions return Python native types:

- `get_available_tool_types()` → `List[str]`
- `get_tool_info(tool_type: str)` → `Dict[str, Any]`
- `get_all_tools_info()` → `Dict[str, Dict[str, Any]]`

### Tool Info Structure

Each tool's information dictionary contains:

```python
{
    "description": str,          # Human-readable description
    "documentation_url": str,    # Link to official documentation
    "required_params": List[str], # Required parameters
    "optional_params": List[str]  # Optional parameters
}
```

## Use Cases

1. **Dynamic Tool Selection**: Discover available tools at runtime and select the best one for your use case
2. **Validation**: Check if a tool exists before attempting to use it
3. **Documentation**: Generate documentation for your application based on available tools
4. **User Interface**: Build dynamic UIs that show users what tools are available
5. **Testing**: Verify that expected tools are available in your environment

## Further Reading

- [Responses API Documentation](https://platform.openai.com/docs/api-reference/responses)
- [Tools Guide](https://platform.openai.com/docs/guides/tools)
- [Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [MCP Tools](https://platform.openai.com/docs/guides/tools-remote-mcp)

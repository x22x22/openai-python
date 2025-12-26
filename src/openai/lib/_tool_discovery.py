"""Tool discovery utilities for the Responses API.

This module provides functions to help users discover what tools are available
for use with the /v1/responses endpoint.
"""

from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal

__all__ = [
    "ToolType",
    "get_available_tool_types",
    "get_tool_info",
    "get_all_tools_info",
]

ToolType = Literal[
    "function",
    "file_search",
    "computer",
    "web_search",
    "mcp",
    "code_interpreter",
    "image_generation",
    "local_shell",
    "function_shell",
    "custom",
    "web_search_preview",
    "apply_patch",
]


def get_available_tool_types() -> List[str]:
    """Get a list of all available tool types for the Responses API.

    Returns:
        A list of tool type strings that can be used in the tools parameter
        when creating a response.

    Example:
        ```python
        from openai.lib import get_available_tool_types

        tool_types = get_available_tool_types()
        print(f"Available tools: {', '.join(tool_types)}")
        ```
    """
    return [
        "function",
        "file_search",
        "computer",
        "web_search",
        "mcp",
        "code_interpreter",
        "image_generation",
        "local_shell",
        "function_shell",
        "custom",
        "web_search_preview",
        "apply_patch",
    ]


def get_tool_info(tool_type: str) -> Dict[str, Any]:
    """Get detailed information about a specific tool type.

    Args:
        tool_type: The type of tool to get information about.

    Returns:
        A dictionary containing information about the tool including its
        description, documentation URL, and required/optional parameters.

    Raises:
        ValueError: If the tool_type is not recognized.

    Example:
        ```python
        from openai.lib import get_tool_info

        info = get_tool_info("web_search")
        print(f"Description: {info['description']}")
        print(f"Learn more: {info['documentation_url']}")
        ```
    """
    tools_info = {
        "function": {
            "description": "Functions that are defined by you, enabling the model to call your own code with strongly typed arguments and outputs.",
            "documentation_url": "https://platform.openai.com/docs/guides/function-calling",
            "required_params": ["type", "function"],
            "optional_params": [],
        },
        "file_search": {
            "description": "A built-in tool for searching through files and documents to find relevant information.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools-file-search",
            "required_params": ["type"],
            "optional_params": ["file_ids", "vector_store_ids", "ranking", "max_results"],
        },
        "computer": {
            "description": "A tool that allows the model to interact with a computer interface.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools",
            "required_params": ["type"],
            "optional_params": ["display_width_px", "display_height_px", "display_number"],
        },
        "web_search": {
            "description": "A built-in tool for searching the web to find current information.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools-web-search",
            "required_params": ["type"],
            "optional_params": ["filters", "user_location"],
        },
        "mcp": {
            "description": "Give the model access to additional tools via remote Model Context Protocol (MCP) servers.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools-remote-mcp",
            "required_params": ["type", "server_label"],
            "optional_params": [
                "server_url",
                "connector_id",
                "allowed_tools",
                "authorization",
                "headers",
                "require_approval",
                "server_description",
            ],
        },
        "code_interpreter": {
            "description": "A tool that runs Python code to help generate a response to a prompt.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools",
            "required_params": ["type", "container"],
            "optional_params": [],
        },
        "image_generation": {
            "description": "A tool that generates images using the GPT image models.",
            "documentation_url": "https://platform.openai.com/docs/guides/images",
            "required_params": ["type"],
            "optional_params": [
                "model",
                "size",
                "quality",
                "background",
                "output_format",
                "output_compression",
                "input_fidelity",
                "input_image_mask",
                "partial_images",
                "moderation",
            ],
        },
        "local_shell": {
            "description": "A tool that allows the model to execute shell commands in a local environment.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools",
            "required_params": ["type"],
            "optional_params": [],
        },
        "function_shell": {
            "description": "A shell-based function tool for executing commands.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools",
            "required_params": ["type"],
            "optional_params": [],
        },
        "custom": {
            "description": "A custom tool defined with specific parameters and behavior.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools",
            "required_params": ["type", "name"],
            "optional_params": ["description"],
        },
        "web_search_preview": {
            "description": "Preview version of the web search tool with additional features.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools-web-search",
            "required_params": ["type"],
            "optional_params": ["filters", "user_location"],
        },
        "apply_patch": {
            "description": "A tool that can apply code patches to files.",
            "documentation_url": "https://platform.openai.com/docs/guides/tools",
            "required_params": ["type"],
            "optional_params": [],
        },
    }

    if tool_type not in tools_info:
        raise ValueError(f"Unknown tool type: {tool_type}. Available types: {', '.join(get_available_tool_types())}")

    return tools_info[tool_type]


def get_all_tools_info() -> Dict[str, Dict[str, Any]]:
    """Get information about all available tools.

    Returns:
        A dictionary mapping tool types to their information.

    Example:
        ```python
        from openai.lib import get_all_tools_info

        all_tools = get_all_tools_info()
        for tool_type, info in all_tools.items():
            print(f"{tool_type}: {info['description']}")
        ```
    """
    return {tool_type: get_tool_info(tool_type) for tool_type in get_available_tool_types()}

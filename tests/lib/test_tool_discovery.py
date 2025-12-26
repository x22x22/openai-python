from __future__ import annotations

import pytest

from openai import get_tool_info, get_all_tools_info, get_available_tool_types


def test_get_available_tool_types():
    """Test that get_available_tool_types returns a list of tool types."""
    tool_types = get_available_tool_types()

    assert isinstance(tool_types, list)
    assert len(tool_types) > 0

    # Check that known tools are in the list
    expected_tools = [
        "function",
        "file_search",
        "computer",
        "web_search",
        "mcp",
        "code_interpreter",
        "image_generation",
        "local_shell",
    ]

    for tool in expected_tools:
        assert tool in tool_types, f"Expected tool '{tool}' not found in available tools"


def test_get_tool_info_web_search():
    """Test getting information about the web_search tool."""
    info = get_tool_info("web_search")

    assert isinstance(info, dict)
    assert "description" in info
    assert "documentation_url" in info
    assert "required_params" in info
    assert "optional_params" in info

    assert isinstance(info["description"], str)
    assert len(info["description"]) > 0
    assert "type" in info["required_params"]


def test_get_tool_info_mcp():
    """Test getting information about the mcp tool."""
    info = get_tool_info("mcp")

    assert isinstance(info, dict)
    assert "description" in info
    assert "documentation_url" in info
    assert "required_params" in info
    assert "optional_params" in info

    assert "type" in info["required_params"]
    assert "server_label" in info["required_params"]
    assert "server_url" in info["optional_params"]
    assert "connector_id" in info["optional_params"]


def test_get_tool_info_code_interpreter():
    """Test getting information about the code_interpreter tool."""
    info = get_tool_info("code_interpreter")

    assert isinstance(info, dict)
    assert "description" in info
    assert "documentation_url" in info
    assert "Python" in info["description"]


def test_get_tool_info_function():
    """Test getting information about the function tool."""
    info = get_tool_info("function")

    assert isinstance(info, dict)
    assert "description" in info
    assert "documentation_url" in info
    assert "function" in info["required_params"]


def test_get_tool_info_file_search():
    """Test getting information about the file_search tool."""
    info = get_tool_info("file_search")

    assert isinstance(info, dict)
    assert "description" in info
    assert "documentation_url" in info
    assert len(info["optional_params"]) > 0


def test_get_tool_info_invalid_tool():
    """Test that get_tool_info raises ValueError for unknown tools."""
    with pytest.raises(ValueError) as exc_info:
        get_tool_info("nonexistent_tool")

    assert "Unknown tool type" in str(exc_info.value)
    assert "nonexistent_tool" in str(exc_info.value)


def test_get_all_tools_info():
    """Test getting information about all tools at once."""
    all_tools = get_all_tools_info()

    assert isinstance(all_tools, dict)
    assert len(all_tools) > 0

    # Check that all tools from get_available_tool_types are included
    available_types = get_available_tool_types()
    for tool_type in available_types:
        assert tool_type in all_tools
        assert isinstance(all_tools[tool_type], dict)
        assert "description" in all_tools[tool_type]
        assert "documentation_url" in all_tools[tool_type]


def test_tool_info_structure():
    """Test that all tool info has the expected structure."""
    all_tools = get_all_tools_info()

    required_keys = ["description", "documentation_url", "required_params", "optional_params"]

    for tool_type, info in all_tools.items():
        for key in required_keys:
            assert key in info, f"Tool '{tool_type}' missing key '{key}'"

        assert isinstance(info["description"], str)
        assert isinstance(info["documentation_url"], str)
        assert isinstance(info["required_params"], list)
        assert isinstance(info["optional_params"], list)

        # All tools should have 'type' as a required parameter
        assert "type" in info["required_params"], f"Tool '{tool_type}' missing 'type' in required_params"


def test_tool_types_match():
    """Test that get_all_tools_info returns info for all available tool types."""
    available_types = get_available_tool_types()
    all_tools = get_all_tools_info()

    assert set(available_types) == set(all_tools.keys())


def test_documentation_urls_valid():
    """Test that all documentation URLs are well-formed."""
    all_tools = get_all_tools_info()

    for tool_type, info in all_tools.items():
        doc_url = info["documentation_url"]
        assert doc_url.startswith("https://"), f"Tool '{tool_type}' has invalid documentation URL"
        assert "platform.openai.com" in doc_url, f"Tool '{tool_type}' documentation URL is not from OpenAI"

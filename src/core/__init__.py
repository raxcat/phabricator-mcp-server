"""Core functionality for the Phabricator MCP Server."""

from .client import PhabricatorClient
from .formatters import (
    format_comments_with_context,
    format_differential_details,
    format_enhanced_differential,
    format_task_details,
    rich_content_to_mcp_blocks,
    rich_content_to_text,
)
from .models import ContentPart, DifferentialInfo, FileInfo, RichContent, TaskInfo

__all__ = [
    "PhabricatorClient",
    "TaskInfo",
    "DifferentialInfo",
    "FileInfo",
    "ContentPart",
    "RichContent",
    "format_task_details",
    "format_differential_details",
    "format_enhanced_differential",
    "format_comments_with_context",
    "rich_content_to_mcp_blocks",
    "rich_content_to_text",
]

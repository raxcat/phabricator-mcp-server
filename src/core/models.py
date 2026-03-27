"""Pydantic models for type safety and validation."""

from pydantic import BaseModel


class TaskInfo(BaseModel):
    """Model for Phabricator task information."""

    id: str
    title: str
    description: str
    status: str
    priority: str
    author_phid: str | None = None
    assigned_phid: str | None = None


class DifferentialInfo(BaseModel):
    """Model for Phabricator differential revision information."""

    id: str
    title: str
    summary: str
    status: str
    author_phid: str


class FileInfo(BaseModel):
    """Metadata and optional content for a Phabricator file (F12345)."""

    file_id: int
    name: str
    mime_type: str
    size: int
    uri: str  # Phabricator page URL, e.g. https://phab.example.com/F12345
    data_uri: str = ""  # Direct download URL
    phid: str = ""
    data_base64: str | None = None  # Base64-encoded content (populated for images)
    is_image: bool = False

    @staticmethod
    def image_mime_types() -> set[str]:
        return {"image/png", "image/jpeg", "image/gif", "image/webp", "image/svg+xml", "image/bmp"}


class ContentPart(BaseModel):
    """A segment of rich content — either plain text or a file reference.

    When reconstructed in order, the list of ContentParts reproduces the
    original document layout with files/images in their original positions.
    """

    type: str  # "text" or "file"
    text: str | None = None  # present when type == "text"
    file: FileInfo | None = None  # present when type == "file"


class RichContent(BaseModel):
    """Text with inline file references resolved into an ordered list of parts.

    Preserves the original position of {Fxxxx} references so consumers can
    render images inline with surrounding text.
    """

    parts: list[ContentPart]
    files: dict[int, FileInfo] = {}  # file_id → FileInfo lookup for convenience

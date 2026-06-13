"""
Request and response schemas for image analysis APIs.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


class ImageUrlListRequest(BaseModel):
    """
    Request schema for APIs that analyze multiple image URLs.
    """

    user_images_urls: list[HttpUrl] = Field(
        ...,
        description="Image URLs used for color, clustering, or matching analysis.",
    )


class CommonRgbResponse(BaseModel):
    """
    Response schema for dominant RGB analysis.
    """

    user_rgb: tuple[int, int, int]
    user_color: str
    user_text: str


class RepresentativeImagesResponse(BaseModel):
    """
    Response schema for representative image selection.
    """

    representative_images: list[str] = Field(default_factory=list)


class AnalysisMetadataResponse(BaseModel):
    """
    Generic response schema for prototype image analysis output.
    """

    result: Any
    message: Optional[str] = None
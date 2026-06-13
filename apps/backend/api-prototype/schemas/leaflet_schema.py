"""
Request and response schemas for mobile leaflet APIs.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


class LeafletCreateRequest(BaseModel):
    """
    Request schema for mobile leaflet generation.

    This schema keeps the prototype input structure based on
    user-captured image URLs.
    """

    user_images_urls: list[HttpUrl] = Field(
        ...,
        description="User-captured artwork image URLs.",
    )


class LeafletArtworkResult(BaseModel):
    """
    Artwork item included in a generated leaflet response.
    """

    url: str
    title: Optional[str] = None
    artist: Optional[str] = None
    description: Optional[str] = None
    color_cluster_ratio: Optional[Any] = None


class LeafletCreateResponse(BaseModel):
    """
    Response schema for mobile leaflet generation.
    """

    matched_urls: list[str] = Field(default_factory=list)
    representative_images: list[str] = Field(default_factory=list)
    dominant_color: Optional[str] = None
    user_color_text: Optional[str] = None
    recommended_artworks: list[LeafletArtworkResult] = Field(default_factory=list)
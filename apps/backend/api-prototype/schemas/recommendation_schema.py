"""
Request and response schemas for artwork recommendation APIs.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


class RecommendationRequest(BaseModel):
    """
    Request schema for space-based artwork recommendation.
    """

    image_url: HttpUrl = Field(
        ...,
        description="User space or interior image URL used for artwork recommendation.",
    )
    preferred_emotions: Optional[list[str]] = Field(
        default=None,
        description="Optional emotion keywords used to refine recommendation results.",
    )
    preferred_colors: Optional[list[str]] = Field(
        default=None,
        description="Optional color names used to refine recommendation results.",
    )


class RecommendationCandidate(BaseModel):
    """
    Candidate artwork returned by the recommendation process.
    """

    artwork_url: str
    title: Optional[str] = None
    artist: Optional[str] = None
    description: Optional[str] = None
    emotions: Optional[list[str]] = None
    color_cluster_ratio: Optional[Any] = None
    score: Optional[float] = None


class RecommendationResponse(BaseModel):
    """
    Response schema for artwork recommendation results.
    """

    recommendations: list[RecommendationCandidate] = Field(default_factory=list)
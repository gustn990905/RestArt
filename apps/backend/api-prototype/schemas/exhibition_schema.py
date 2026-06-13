"""
Request and response schemas for exhibition recommendation APIs.
"""

from typing import Optional

from pydantic import BaseModel, Field


class NearbyExhibitionRequest(BaseModel):
    """
    Request schema for nearby exhibition recommendation.

    This schema keeps the prototype input structure based on latitude
    and longitude values.
    """

    lat_input: float = Field(
        ...,
        description="Current user latitude.",
    )
    long_input: float = Field(
        ...,
        description="Current user longitude.",
    )
    radius_km: float = Field(
        default=5.0,
        description="Search radius in kilometers.",
    )


class ExhibitionItem(BaseModel):
    """
    Exhibition item returned by exhibition recommendation APIs.
    """

    name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    image_url: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    distance_km: Optional[float] = None


class NearbyExhibitionResponse(BaseModel):
    """
    Response schema for nearby exhibition recommendation.
    """

    exhibitions: list[ExhibitionItem] = Field(default_factory=list)
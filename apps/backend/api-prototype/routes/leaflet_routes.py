"""
Route factory for mobile leaflet APIs.

This module prepares the route layer for the existing leaflet creation
prototype logic. Runtime dependencies are passed from the main backend
module to avoid circular imports.
"""

from typing import Any, Callable

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.leaflet_service import create_leaflet_service


def build_leaflet_router(
    get_db_dependency: Callable,
    image_data_model: Any,
    color_dict: dict,
    find_matching_images_fn: Callable,
    analyze_images_and_cluster_fn: Callable,
    find_signiture_color_fn: Callable,
    exact_match_fn: Callable,
    count_matches_fn: Callable,
    random_exhibition_fn: Callable,
    leaflet_design_fn: Callable,
) -> APIRouter:
    """
    Build leaflet router using existing prototype dependencies.

    Parameters
    ----------
    get_db_dependency:
        Existing backend database dependency.
    image_data_model:
        Existing prototype request model containing user image URLs.
    color_dict:
        Existing prototype color dictionary.
    find_matching_images_fn:
        Existing image matching function.
    analyze_images_and_cluster_fn:
        Existing representative image selection function.
    find_signiture_color_fn:
        Existing signature color function.
    exact_match_fn:
        Existing exact emotion matching function.
    count_matches_fn:
        Existing partial emotion matching function.
    random_exhibition_fn:
        Existing random exhibition function.
    leaflet_design_fn:
        Existing leaflet design mapping function.

    Returns
    -------
    APIRouter
        FastAPI router for leaflet endpoints.
    """
    router = APIRouter(tags=["leaflet"])
    ImageDataModel = image_data_model

    @router.post("/leaflet_creating/")
    async def leaflet_creating(
        image_data: ImageDataModel,
        db: Session = Depends(get_db_dependency),
    ):
        return create_leaflet_service(
            image_data=image_data,
            db=db,
            color_dict=color_dict,
            find_matching_images_fn=find_matching_images_fn,
            analyze_images_and_cluster_fn=analyze_images_and_cluster_fn,
            find_signiture_color_fn=find_signiture_color_fn,
            exact_match_fn=exact_match_fn,
            count_matches_fn=count_matches_fn,
            random_exhibition_fn=random_exhibition_fn,
            leaflet_design_fn=leaflet_design_fn,
        )

    return router
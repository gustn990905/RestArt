"""
Route factory for nearby exhibition APIs.

This module prepares the route layer for the existing nearby exhibition
prototype logic. Runtime dependencies are passed from the main backend
module to avoid circular imports.
"""

from typing import Any, Callable

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from services.exhibition_service import find_near_exhibition_service


def build_exhibition_router(
    get_db_dependency: Callable,
    lat_long_model: Any,
    find_nearby_exhibitions_fn: Callable,
) -> APIRouter:
    """
    Build exhibition router using existing prototype dependencies.

    Parameters
    ----------
    get_db_dependency:
        Existing backend database dependency.
    lat_long_model:
        Existing latitude/longitude request model from the prototype.
    find_nearby_exhibitions_fn:
        Existing nearby exhibition function imported from the prototype
        image utility.

    Returns
    -------
    APIRouter
        FastAPI router for nearby exhibition endpoints.
    """
    router = APIRouter(tags=["exhibition"])

    @router.get("/find_near_exhibition/")
    async def find_near_exhibition(
        lat_input: float = Query(...),
        long_input: float = Query(...),
        db: Session = Depends(get_db_dependency),
    ):
        return find_near_exhibition_service(
            lat_input=lat_input,
            long_input=long_input,
            db=db,
            lat_long_model=lat_long_model,
            find_nearby_exhibitions_fn=find_nearby_exhibitions_fn,
        )

    return router
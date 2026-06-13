"""
Service logic for nearby exhibition recommendation.

This module separates the existing nearby exhibition logic from the
backend prototype endpoint while preserving the original data flow.
"""

from typing import Any

from sqlalchemy import text


def find_near_exhibition_service(
    lat_input: float,
    long_input: float,
    db: Any,
    lat_long_model: Any,
    find_nearby_exhibitions_fn: Any,
) -> dict:
    """
    Find the nearest exhibition based on the existing prototype logic.

    Parameters
    ----------
    lat_input:
        User latitude.
    long_input:
        User longitude.
    db:
        SQLAlchemy database session used by the backend prototype.
    lat_long_model:
        Existing prototype Pydantic model used for latitude/longitude list.
    find_nearby_exhibitions_fn:
        Existing nearby exhibition function imported from the prototype
        image utility.

    Returns
    -------
    dict
        Detailed exhibition information.
    """
    exhibition_all = db.execute(text("SELECT name FROM exhibitions")).fetchall()
    exhibition = [row[0] for row in exhibition_all]

    exhibition_all2 = db.execute(text("SELECT latitude FROM exhibitions")).fetchall()
    exhibition2 = [row[0] for row in exhibition_all2]

    exhibition_all3 = db.execute(text("SELECT longitude FROM exhibitions")).fetchall()
    exhibition3 = [row[0] for row in exhibition_all3]

    exhibition_info = [
        [exhibition[i], [float(exhibition2[i]), float(exhibition3[i])]]
        for i in range(len(exhibition))
    ]

    user_location = [lat_input, long_input]
    location_ex = lat_long_model(lat_long_list=user_location)

    radius = 100
    nearest_exhibition_name = find_nearby_exhibitions_fn(
        location_ex.lat_long_list,
        exhibition_info,
        radius,
    )

    result = db.execute(
        text(
            """
            SELECT start_date, end_date, description, exhibition_img
            FROM exhibitions
            WHERE name = :name
            """
        ),
        {"name": nearest_exhibition_name},
    ).mappings().fetchone()

    detailed_exhibition = {}

    if result:
        detailed_exhibition = {
            "name": nearest_exhibition_name,
            "start_date": result["start_date"],
            "end_date": result["end_date"],
            "description": result["description"],
            "exhibition_img": result["exhibition_img"],
        }

    return detailed_exhibition
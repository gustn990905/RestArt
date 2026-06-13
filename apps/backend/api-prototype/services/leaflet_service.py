"""
Service logic for mobile leaflet generation.

This module separates the existing leaflet creation logic from the
backend prototype endpoint while preserving the original matching,
color extraction, artwork recommendation, and exhibition recommendation
flow.
"""

import json
import random
from typing import Any

from fastapi import HTTPException
from sqlalchemy import text


def create_leaflet_service(
    image_data: Any,
    db: Any,
    color_dict: dict,
    find_matching_images_fn: Any,
    analyze_images_and_cluster_fn: Any,
    find_signiture_color_fn: Any,
    exact_match_fn: Any,
    count_matches_fn: Any,
    random_exhibition_fn: Any,
    leaflet_design_fn: Any,
) -> dict:
    """
    Create a mobile leaflet result based on the existing prototype logic.

    Parameters
    ----------
    image_data:
        Existing prototype request object containing user_images_urls.
    db:
        SQLAlchemy database session used by the backend prototype.
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
    dict
        Leaflet result used by the backend prototype.
    """
    result_urls = db.execute(text("SELECT url FROM images_exhibition_13")).fetchall()
    row_images = [row[0] for row in result_urls]

    result_ratios = db.execute(
        text("SELECT color_cluster_ratio FROM images_exhibition_13")
    ).fetchall()
    row_images2 = [row[0] for row in result_ratios]

    result = {
        "url": row_images,
        "color_cluster_ratio": row_images2,
    }

    try:
        matching_images_response = find_matching_images_fn(image_data, result)
        matching_urls = matching_images_response["matching_urls"]

        analysis_result = analyze_images_and_cluster_fn(
            matching_urls,
            result,
        )

        if matching_urls["url"] != []:
            color_number_one = find_signiture_color_fn(
                matching_urls["color_cluster_ratio"]
            )
        else:
            color_number_one = find_signiture_color_fn(
                random.choices(result["color_cluster_ratio"], k=4)
            )

        text_user = {}

        dominant_color = None
        user_rgb = None

        for color_name in color_dict.keys():
            if color_name == color_number_one:
                text_user = {"user_color": color_dict[color_name][1]}
                dominant_color = color_name
                user_rgb = color_dict[color_name][0]
                break

        rrow = db.execute(text("SELECT * FROM images_exhibition_1")).mappings().all()

        result_urls = db.execute(text("SELECT url FROM images_exhibition_1")).fetchall()
        row2 = [row[0] for row in result_urls]

        result_ratios = db.execute(
            text("SELECT color_cluster_ratio FROM images_exhibition_1")
        ).fetchall()
        row3 = [row[0] for row in result_ratios]

        new_color_dict = {}
        jj = 0

        for image_url in row2:
            new_color_dict[image_url] = json.loads(row3[jj])
            jj += 1

        recommend_picture = None

        mood_dict = {}

        for index in range(len(rrow)):
            mood_dict[rrow[index]["url"]] = rrow[index]["emotions"]

        max_color = 0

        for key, colors in new_color_dict.items():
            for color in colors:
                if color[0] == dominant_color:
                    if color[2] > max_color:
                        max_color = color[2]
                        recommend_picture = key

        recommend_picture_list = []

        if recommend_picture:
            for index in range(len(new_color_dict)):
                if recommend_picture == rrow[index]["url"]:
                    recommend_picture_list.append(rrow[index]["url"])
                    recommend_picture_list.append(rrow[index]["title"])
                    recommend_picture_list.append(rrow[index]["author"])
        else:
            no_no = random.randint(1, len(rrow))
            recommend_picture_list.append(rrow[no_no]["url"])
            recommend_picture_list.append(rrow[no_no]["title"])
            recommend_picture_list.append(rrow[no_no]["author"])
            recommend_picture = rrow[no_no]["url"]

        target_mood = mood_dict[recommend_picture]

        del mood_dict[recommend_picture]

        all_three_matches = [
            key for key, value in mood_dict.items()
            if exact_match_fn(value, target_mood)
        ]

        if all_three_matches:
            result_picture = random.choice(all_three_matches)
        else:
            two_matches = [
                key for key, value in mood_dict.items()
                if count_matches_fn(value, target_mood) == 2
            ]

            if two_matches:
                result_picture = random.choice(two_matches)
            else:
                one_match = [
                    key for key, value in mood_dict.items()
                    if count_matches_fn(value, target_mood) == 1
                ]

                if one_match:
                    result_picture = random.choice(one_match)
                else:
                    result_picture = None

        recommend_picture_list2 = []

        for index in range(len(mood_dict)):
            if result_picture == rrow[index]["url"]:
                recommend_picture_list2.append(rrow[index]["url"])
                recommend_picture_list2.append(rrow[index]["title"])
                recommend_picture_list2.append(rrow[index]["author"])

        exhibition = db.execute(
            text(
                """
                SELECT *
                FROM exhibitions
                WHERE exhibition_id = :id1 OR exhibition_id = :id2
                """
            ),
            {"id1": 11, "id2": 12},
        ).mappings().all()

        recom_exhibition = random_exhibition_fn(exhibition)

        leaflet_color = leaflet_design_fn(str(dominant_color))
        text_user["leaflet_design"] = leaflet_color

        text_user["user_rgb"] = user_rgb
        text_user["recom_picture1"] = recommend_picture_list
        text_user["recom_picture2"] = recommend_picture_list2
        text_user["spectral_key"] = [analysis_result]
        text_user["recom_exhibition"] = recom_exhibition

        return text_user

    except HTTPException as error:
        raise error

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
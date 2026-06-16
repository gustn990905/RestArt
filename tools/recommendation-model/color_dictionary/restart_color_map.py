"""
RestArt color map.

This module stores RestArt color names and representative RGB values
used in the recommendation prototype.

The color map is used to connect extracted image colors with
RestArt-defined color names.
"""

from __future__ import annotations

from math import sqrt


restart_color_map: dict[str, tuple[int, int, int]] = {
    "Cinnabar": (207, 46, 49),
    "Guardsman Red": (172, 35, 48),
    "Tonys Pink": (233, 163, 144),
    "Terra Cotta": (231, 108, 86),
    "Almond": (236, 217, 202),
    "Clam Shell": (213, 182, 166),
    "Feldspar": (211, 142, 110),
    "Hemp": (171, 131, 115),
    "Tuscany": (162, 88, 61),
    "Tamarillo": (116, 47, 50),
    "Cioccolato": (115, 63, 44),
    "Pumpkin": (238, 113, 25),
    "Harvest Gold": (241, 176, 102),
    "Yellow": (255, 200, 8),
    "Paris Daisy": (255, 228, 15),
    "Bahia": (170, 198, 27),
    "Manz": (219, 220, 93),
    "Forest Green": (19, 166, 50),
    "Mantis": (146, 198, 131),
    "Salem": (4, 148, 87),
    "Camarone": (39, 122, 62),
    "Eastern Blue": (1, 134, 141),
    "Genoa": (53, 109, 98),
    "Cobalt": (3, 86, 155),
    "Cerulean": (6, 113, 148),
    "Persian Indigo": (46, 20, 141),
    "Black": (0, 0, 0),
    "White Smoke": (244, 244, 244),
    "Very Light Grey": (206, 206, 206),
    "Grey": (152, 152, 152),
    "Deep Koamaru": (40, 47, 103),
    "Palm Green": (34, 62, 51),
    "Corn Field": (245, 223, 181),
    "Fun Green": (24, 89, 63),
    "Sherpa Blue": (8, 87, 107),
    "Wistful": (197, 188, 213),
    "Granny Smith": (127, 175, 166),
    "Nepal": (147, 184, 213),
    "Rose": (218, 176, 176),
    "Granite Green": (144, 135, 96),
    "Dingley": (88, 126, 61),
    "Costa Del Sol": (139, 117, 65),
    "Mandy": (204, 63, 92),
    "Pale Sky": (92, 104, 106),
    "Au Chico": (175, 97, 87),
    "London Hue": (178, 137, 166),
    "Cabaret": (209, 100, 109),
    "Seagull": (126, 188, 209),
    "Frostee": (221, 232, 207),
    "Aqua Squeeze": (209, 234, 211),
    "Pattens Blue": (194, 222, 242),
    "Hawkes Blue": (203, 215, 232),
    "Titan White": (224, 218, 230),
    "Pale Rose": (235, 219, 224),
    "Raffia": (218, 196, 148),
    "Red Damask": (209, 116, 73),
    "Sprout": (179, 202, 157),
    "Spring Rain": (166, 201, 163),
    "Heather": (165, 184, 199),
    "Wafer": (206, 185, 179),
    "Sage": (143, 162, 121),
    "Oxley": (122, 165, 123),
    "Lemon Ginger": (156, 137, 37),
    "Tosca": (115, 71, 79),
    "Green House": (54, 88, 48),
}


def get_rgb(color_name: str) -> tuple[int, int, int] | None:
    """Return the representative RGB value for a RestArt color name."""
    return restart_color_map.get(color_name)


def list_color_names() -> list[str]:
    """Return all registered RestArt color names."""
    return list(restart_color_map.keys())


def color_distance(
    rgb_a: tuple[int, int, int],
    rgb_b: tuple[int, int, int],
) -> float:
    """Calculate Euclidean distance between two RGB values."""
    return sqrt(
        (rgb_a[0] - rgb_b[0]) ** 2
        + (rgb_a[1] - rgb_b[1]) ** 2
        + (rgb_a[2] - rgb_b[2]) ** 2
    )


def find_nearest_color(rgb: tuple[int, int, int]) -> tuple[str, tuple[int, int, int], float]:
    """
    Find the nearest RestArt color for an RGB value.

    Returns:
        A tuple of color name, representative RGB value, and distance.
    """
    if not restart_color_map:
        raise ValueError("RestArt color map is empty.")

    nearest_name = ""
    nearest_rgb = (0, 0, 0)
    nearest_distance = float("inf")

    for color_name, color_rgb in restart_color_map.items():
        distance = color_distance(rgb, color_rgb)

        if distance < nearest_distance:
            nearest_name = color_name
            nearest_rgb = color_rgb
            nearest_distance = distance

    return nearest_name, nearest_rgb, nearest_distance
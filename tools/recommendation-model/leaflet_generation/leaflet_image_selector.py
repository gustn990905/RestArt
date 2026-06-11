"""
Leaflet image selection utility from the RestArt recommendation prototype.

This module is based on the original leaflet-related logic in image_utils.py.
It selects representative leaflet images, extracts a signature color from
matched artwork color data, and maps the dominant color to a leaflet design type.

Note:
- The original prototype uses the function name `find_signiture_color`.
- The typo is intentionally preserved here to avoid breaking references from the prototype.
"""

import json
import random

import numpy as np

from scipy.spatial.distance import cdist
from sklearn.cluster import SpectralClustering


def gaussian_kernel(x, y, sigma=1.0):
    return np.exp(-np.linalg.norm(x - y) ** 2 / (2 * (sigma ** 2)))


def analyze_images_and_cluster(user_images_urls, result, num_clusters_spectral: int = 4, sigma: float = 30):
    if len(user_images_urls['url']) > 4:
        final_dict = {}
        kkk = 0

        for image_url in user_images_urls['url']:
            final_dict[image_url] = tuple(json.loads(user_images_urls['color_cluster_ratio'][kkk])[0][1])
            kkk += 1

        rgb_colors = [value for value in final_dict.values()]
        rgb_colors_array = np.array(rgb_colors)
        n_samples = len(rgb_colors)

        similarity_matrix = np.zeros((n_samples, n_samples))

        for i in range(n_samples):
            for j in range(n_samples):
                similarity_matrix[i, j] = gaussian_kernel(rgb_colors_array[i], rgb_colors_array[j], sigma)

        spectral = SpectralClustering(n_clusters=num_clusters_spectral, affinity='precomputed')
        labels = spectral.fit_predict(similarity_matrix)

        cluster_centers = np.array(
            [
                rgb_colors_array[labels == i].mean(axis=0)
                for i in range(num_clusters_spectral)
            ],
            dtype=int
        )

        target_keys = []
        selected_keys = set()

        for center in cluster_centers:
            distances = cdist([center], rgb_colors_array, metric='euclidean')[0]
            closest_index = np.argmin(distances)
            closest_color = rgb_colors_array[closest_index]

            rgb_colors_array = np.delete(rgb_colors_array, closest_index, axis=0)

            possible_keys = [
                key
                for key, value in final_dict.items()
                if np.array_equal(value, closest_color)
            ]
            possible_keys = [
                key
                for key in possible_keys
                if key not in selected_keys
            ]

            if possible_keys:
                selected_key = np.random.choice(possible_keys)
                selected_keys.add(selected_key)
                target_keys.append(selected_key)

    elif len(user_images_urls['url']) == 4:
        target_keys = list(set(user_images_urls['url']))

    elif user_images_urls['url'] == []:
        target_keys = list(set(random.sample(result['url'], k=4)))

    elif len(user_images_urls['url']) == 3:
        target_keys = list(set(user_images_urls['url']))
        result2 = [url for url in result['url'] if url not in target_keys]
        target_keys.append(random.sample(result2, k=1)[0])

    elif len(user_images_urls['url']) == 2:
        target_keys = list(set(user_images_urls['url']))
        result2 = [url for url in result['url'] if url not in target_keys]
        result3 = random.sample(result2, k=2)

        for i in range(2):
            target_keys.append(result3[i])

    else:
        target_keys = list(set(user_images_urls['url']))
        result2 = [url for url in result['url'] if url not in target_keys]
        result3 = random.sample(result2, k=3)

        for i in range(3):
            target_keys.append(result3[i])

    return list(set(target_keys))


def find_signiture_color(user_images_urls, num_clusters=10):
    color_list = []

    for i in range(len(user_images_urls)):
        color_list.append(json.loads(user_images_urls[i]))

    color_final_list = []

    for image_colors in color_list:
        for color_info in image_colors:
            color_dict = {}
            color_dict[color_info[0]] = color_info[3]
            color_final_list.append(color_dict)

    signiture_color = {}

    for item in color_final_list:
        for key, value in item.items():
            if key in signiture_color:
                signiture_color[key] += value
            else:
                signiture_color[key] = value

    final_signiture_color = sorted(
        signiture_color.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return final_signiture_color[0][0]


List1 = [
    "Cinnabar",
    "Brandy Rose",
    "Granite Green",
    "Cioccolato",
    "Deep Bronze",
    "Metallic Copper",
    "Tamarillo",
    "Apple Blossom",
    "Feldspar",
    "Vesuvius",
    "Tonys Pink",
    "Lemon Ginger",
    "Guardsman Red",
    "Mandy",
    "Costa Del Sol",
]

List2 = [
    "Black",
    "Matterhorn",
    "Nobel",
    "Very Light Grey",
    "White Smoke",
    "Wistful",
    "Tiber",
    "Wafer",
    "Pale Rose",
    "Oyster Pink",
    "Opal",
    "Aqua Squeeze",
    "Oxley",
]

List3 = [
    "Paris Daisy",
    "Corn Field",
    "Kournikova",
    "Tangerine Yellow",
    "Persian Indigo",
    "Cobalt",
    "Manz",
    "Cerulean",
    "Vida Loca",
    "Granny Smith",
    "Wheat",
    "Chetwode Blue",
    "Siam",
    "Seagull",
    "Gulf Stream",
    "Heather",
    "Hawkes Blue",
]

List4 = [
    "Bahia",
    "Gossip",
    "Pumpkin",
    "Harvest Gold",
    "Dark Pastel Green",
    "Shamrock Green",
    "Salem",
    "Eastern Blue",
    "Wild Willow",
    "Chelsea Cucumber",
    "Fun Green",
    "Deep Teal",
    "Timber Green",
    "Palm Green",
    "Surfie Green",
    "Blue Lagoon",
    "Camarone",
    "Green House",
    "Sprout",
    "London Hue",
]


def leaflet_design(dominant_color):
    if dominant_color in List1:
        return 1
    elif dominant_color in List2:
        return 2
    elif dominant_color in List3:
        return 3
    else:
        return 4
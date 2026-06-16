# -*- coding: cp949 -*-
import math
import numpy as np
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import defaultdict

RestArt_color = {
    ((207, 46, 49), (231, 47, 39)): "Cinnabar",
    (172, 35, 48): "Guardsman Red",
    (233, 163, 144): "Tonys Pink",
    (231, 108, 86): "Terra Cotta",
    (236, 217, 202): "Almond",
    (213, 182, 166): "Clam Shell",
    ((211, 142, 110), (215, 145, 96)): "Feldspar",
    ((171, 131, 115), (158, 128, 110), (148, 133, 105), (160, 147, 131)): "Hemp",
    ((162, 88, 61), (167, 100, 67), (169, 87, 49)): "Tuscany",
    ((116, 47, 50), (111, 61, 56)): "Tamarillo",
    ((115, 63, 44), (79, 46, 43), (85, 55, 43), (75, 63, 45), (88, 60, 50)): "Cioccolato",
    ((238, 113, 25), (226, 132, 45)): "Pumpkin",
    ((241, 176, 102), (242, 178, 103)): "Harvest Gold",
    ((255, 200, 8), (227, 189, 28), (255, 203, 88), (155, 196, 113)): "Yellow",
    ((255, 228, 15), (255, 236, 79)): "Paris Daisy",
    ((170, 198, 27), (162, 179, 36), (169, 199, 35), (195, 202, 101)): "Bahia",
    (219, 220, 93): "Manz",
    ((19, 166, 50), (18, 154, 47), (88, 171, 45)): "Forest Green",
    ((146, 198, 131), (141, 188, 90), (140, 195, 110)): "Mantis",
    ((4, 148, 87), (6, 134, 84), (43, 151, 89)): "Salem",
    ((39, 122, 62), (23, 106, 43), (20, 114, 48), (30, 98, 50)): "Camarone",
    ((1, 134, 141), (3, 130, 122), (0, 147, 159), (117, 173, 169)): "Eastern Blue",
    (53, 109, 98): "Genoa",
    ((3, 86, 155), (44, 77, 143)): "Cobalt",
    ((6, 113, 148), (59, 130, 157)): "Cerulean",
    ((46, 20, 141), (58, 55, 119)): "Persian Indigo",
    ((44, 60, 49), (53, 52, 48), (60, 60, 60), (38, 38, 38), (10, 10, 10)): "Black",
    ((244, 244, 244), (236, 236, 236)): "White Smoke",
    ((206, 206, 206), (180, 180, 180), (184, 190, 189), (151, 150, 139)): "Very Light Grey",
    ((152, 152, 152), (126, 126, 126), (86, 86, 86)): "Grey",
    ((40, 47, 103), (34, 54, 68)): "Deep Koamaru",
    ((34, 62, 51), (31, 56, 45), (29, 60, 47), (25, 62, 63)): "Palm Green",
    ((245, 223, 181), (228, 235, 191), (233, 227, 143), (249, 239, 189)): "Corn Field",
    ((24, 89, 63), (20, 88, 60), (18, 83, 65), (27, 86, 49)): "Fun Green",
    ((8, 87, 107), (16, 76, 84)): "Sherpa Blue",
    ((197, 188, 213), (170, 165, 199)): "Wistful",
    ((127, 175, 166), (130, 154, 145), (133, 154, 153)): "Granny Smith",
    ((147, 184, 213), (138, 166, 187)): "Nepal",
    ((218, 176, 176), (205, 154, 149)): "Rose",
    ((144, 135, 96), (109, 116, 73)): "Granite Green",
    ((88, 126, 61), (91, 132, 47)): "Dingley",
    ((139, 117, 65), (103, 91, 44)): "Costa Del Sol",
    (204, 63, 92): "Mandy",
    (92, 104, 106): "Pale Sky",
    (175, 97, 87): "Au Chico",
    (178, 137, 166): "London Hue",
    (209, 100, 109): "Cabaret",
    (126, 188, 209): "Seagull",
    (221, 232, 207): "Frostee",
    (209, 234, 211): "Aqua Squeeze",
    (194, 222, 242): "Pattens Blue",
    (203, 215, 232): "Hawkes Blue",
    (224, 218, 230): "Titan White",
    (235, 219, 224): "Pale Rose",
    (218, 196, 148): "Raffia",
    (209, 116, 73): "Red Damask",
    (179, 202, 157): "Sprout",
    (166, 201, 163): "Spring Rain",
    (165, 184, 199): "Heather",
    (206, 185, 179): "Wafer",
    (143, 162, 121): "Sage",
    (122, 165, 123): "Oxley",
    (156, 137, 37): "Lemon Ginger",
    (115, 71, 79): "Tosca",
    (54, 88, 48): "Green House"
}


def extract_top_colors_and_save_clustered_image(image_path, num_clusters):
    image = Image.open(image_path)
    image = image.convert('RGB')
    np_image = np.array(image)
    pixels = np_image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.round(0).astype(np.uint8)
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    total_count = np.sum(counts)
    color_ratios = [(colors[i], counts[i] / total_count) for i in labels]
    color_ratios_sorted = sorted(color_ratios, key=lambda x: x[1], reverse=True)
    return color_ratios_sorted

image_path = "C:/Users/asdfg/source/repos/practice/images/aaa.jpg"
num_clusters = 10 
top_colors = extract_top_colors_and_save_clustered_image(image_path, num_clusters)

def colormatching(randomrgb):
    def euclidean_distance(rgb1, rgb2):
        return np.sqrt(np.sum((np.array(rgb1) - np.array(rgb2))**2))
    min_distance = float('inf')
    closest_color_name = None
    closest_color_rgb = None
    for color_set, color_name in RestArt_color.items():
        if isinstance(color_set, tuple) and isinstance(color_set[0], tuple):
            for color in color_set:
                distance = euclidean_distance(randomrgb, color)
                if distance < min_distance:
                    min_distance = distance
                    closest_color_name = color_name
                    closest_color_rgb = color
        elif isinstance(color_set, tuple):
            distance = euclidean_distance(randomrgb, color_set)
            if distance < min_distance:
                min_distance = distance
                closest_color_name = color_name
                closest_color_rgb = color_set
    return closest_color_name, closest_color_rgb

color_info = defaultdict(int)
for color, ratio in top_colors:
    randomrgb = color
    color_name, color_rgb = colormatching(randomrgb)
    color_info[color_name] += 1

# ���� ���� ���ε� ���� �̸� ã��
most_frequent_color_name = max(color_info, key=color_info.get)
most_frequent_count = color_info[most_frequent_color_name]
print(f"Most frequent color name: {most_frequent_color_name} with {most_frequent_count} occurrences.")

# ��� ���ε� ���� ���� ���
for color_name, count in color_info.items():
    print(f"Color Name: {color_name}, Count: {count}")
    

color_info = defaultdict(lambda: {'rgb': None, 'ratio': 0})
for color, ratio in top_colors:
    randomrgb = color
    color_name, color_rgb = colormatching(randomrgb)
    if color_info[color_name]['rgb'] is None:
        color_info[color_name]['rgb'] = color_rgb
    color_info[color_name]['ratio'] += ratio

sorted_color_info = sorted(color_info.items(), key=lambda item: item[1]['ratio'], reverse=True)

for color_name, info in sorted_color_info:
    first_color = next(iter(RestArt_color.keys()))
    for key in RestArt_color:
        if isinstance(key, tuple) and isinstance(key[0], tuple):
            if color_name == RestArt_color[key]:
                first_color = key[0]
                break
        elif isinstance(key, tuple):
            if color_name == RestArt_color[key]:
                first_color = key
                break
    print(f"Closest color name: {color_name}, RGB: {first_color}, Total Ratio: {info['ratio']:.3f}")
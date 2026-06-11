import requests
import numpy as np

from io import BytesIO
from PIL import Image
from sklearn.cluster import KMeans


RestArt_color = {
        ((231, 47, 39), (207, 46, 49)): "Cinnabar",
        ((38, 38, 38), (10, 10, 10)): "Black",
        ((86, 86, 86), (60, 60, 60)): "Matterhorn",
        ((152, 152, 152), (126, 126, 126)): "Nobel",
        ((206, 206, 206), (180, 180, 180)): "Very Light Grey",
        ((244, 244, 244), (236, 236, 236)): "White Smoke",
        ((255, 228, 15), (255, 236, 79)): "Paris Daisy",
        ((249, 239, 189), (228, 235, 191)): "Corn Field",
        ((170, 198, 27), (169, 199, 35)): "Bahia",
        ((155, 196, 113), (255, 203, 88)): "Kournikova",
        ((146, 198, 131), (140, 195, 110)): "Gossip",
        ((255, 200, 8), (227, 189, 28)): "Tangerine Yellow",
        ((238, 113, 25), (226, 132, 45)): "Pumpkin",
        ((241, 176, 102), (242, 178, 103)): "Harvest Gold",
        ((46, 20, 141), (58, 55, 119)): "Persian Indigo",
        ((3, 86, 155), (44, 77, 143)): "Cobalt",
        ((19, 166, 50), (18, 154, 47)): "Dark Pastel Green",
        ((4, 148, 87), (43, 151, 89)): "Shamrock Green",
        ((6, 134, 84), (39, 122, 62)): "Salem",
        ((197, 188, 213), (170, 165, 199)): "Wistful",
        ((1, 134, 141), (0, 147, 159)): "Eastern Blue",
        ((171, 131, 115), (158, 128, 110)): "Brandy Rose",
        ((148, 133, 105), (144, 135, 96)): "Granite Green",
        ((219, 220, 93), (233, 227, 143)): "Manz",
        ((162, 179, 36), (195, 202, 101)): "Wild Willow",
        ((79, 46, 43), (88, 60, 50)): "Cioccolato",
        ((6, 113, 148), (59, 130, 157)): "Cerulean",
        ((88, 171, 45), (141, 188, 90)): "Chelsea Cucumber",
        ((24, 89, 63), (20, 88, 60)): "Fun Green",
        ((27, 86, 49), (18, 83, 65)): "Deep Teal",
        ((75, 63, 45), (53, 52, 48)): "Deep Bronze",
        ((44, 60, 49), (34, 62, 51)): "Timber Green",
        ((31, 56, 45), (29, 60, 47)): "Palm Green",
        ((25, 62, 63), (34, 54, 68)): "Tiber",
        ((85, 55, 43), (111, 61, 56)): "Metallic Copper",
        ((116, 47, 50), (115, 71, 79)): "Tamarillo",
        ((175, 92, 87), (162, 88, 61)): "Apple Blossom",
        ((3, 130, 122), (53, 109, 98)): "Surfie Green",
        ((211, 142, 110), (215, 145, 96)): "Feldspar",
        ((167, 100, 67), (169, 87, 49)): "Vesuvius",
        ((8, 87, 107), (16, 76, 84)): "Blue Lagoon",
        ((231, 108, 86), (233, 163, 144)): "Tonys Pink",
        ((213, 182, 166), (206, 185, 179)): "Wafer",
        ((20, 114, 48), (30, 98, 50)): "Camarone",
        ((88, 126, 61), (91, 132, 47)): "Vida Loca",
        ((54, 88, 48), (23, 106, 43)): "Green House",
        ((130, 154, 145), (133, 154, 153)): "Granny Smith",
        ((245, 223, 181), (218, 196, 148)): "Wheat",
        ((236, 217, 202), (235, 219, 224)): "Pale Rose",
        ((218, 176, 176), (205, 154, 149)): "Oyster Pink",
        ((184, 190, 189), (151, 150, 139)): "Opal",
        ((178, 137, 166), (224, 218, 230)): "London Hue",
        ((139, 117, 65), (156, 137, 37)): "Lemon Ginger",
        ((172, 36, 48), (115, 63, 44)): "Guardsman Red",
        ((204, 63, 92), (209, 100, 109)): "Mandy",
        ((160, 147, 131), (103, 91, 44)): "Costa Del Sol",
        ((92, 104, 163), (40, 57, 103)): "Chetwode Blue",
        ((221, 232, 207), (209, 234, 211)): "Aqua Squeeze",
        ((209, 116, 73), (109, 116, 73)): "Siam",
        ((179, 202, 157), (143, 162, 121)): "Sprout",
        ((166, 201, 163), (122, 165, 123)): "Oxley",
        ((126, 188, 209), (194, 222, 242)): "Seagull",
        ((127, 175, 166), (117, 173, 169)): "Gulf Stream",
        ((165, 184, 199), (138, 166, 187)): "Heather",
        ((147, 184, 213), (203, 215, 232)): "Hawkes Blue"
    }

def get_images_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def extract_top_colors(image, num_clusters):
    #image = Image.open(image)
    image = image.convert('RGB')
    np_image = np.array(image)
    pixels = np_image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.round(0).astype(np.uint8)
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    total_count = np.sum(counts)
    color_ratios = [(colors[i], counts[i] / total_count) for i in labels]
    return sorted(color_ratios, key=lambda x: x[1], reverse=True)

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
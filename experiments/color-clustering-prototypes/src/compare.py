# -*- coding: cp949 -*-

db = [
    [[[186, 130, 35], 0.186], [[200, 44, 45], 0.186], [[167, 34, 38], 0.159], [[124, 26, 29], 0.11], [[122, 100, 30], 0.095], [[82, 73, 31], 0.075], [[210, 90, 70], 0.073], [[69, 24, 22], 0.07], [[85, 108, 63], 0.023], [[211, 140, 113], 0.023]],
    [[[230, 220, 216], 0.334], [[215, 193, 186], 0.202], [[32, 9, 7], 0.106], [[219, 136, 133], 0.078], [[96, 40, 30], 0.077], [[151, 166, 160], 0.066], [[136, 100, 94], 0.057], [[201, 52, 53], 0.035], [[47, 107, 127], 0.026], [[241, 193, 47], 0.018]],
    [[[64, 53, 15], 0.162], [[86, 69, 5], 0.158], [[200, 154, 13], 0.134], [[108, 100, 11], 0.1], [[85, 76, 41], 0.086], [[138, 106, 49], 0.085], [[126, 75, 17], 0.083], [[168, 117, 9], 0.074], [[214, 172, 102], 0.063], [[187, 131, 76], 0.057]]
]


from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def extract_top_colors_and_save_clustered_image(image_path, num_clusters=3, save_path='clustered_image.png'):
    # 이미지를 열고 RGB로 변환
    image = Image.open(image_path)
    image = image.convert('RGB')

    # 이미지 데이터를 numpy 배열로 변환
    np_image = np.array(image)
    pixels = np_image.reshape(-1, 3)  # 픽셀을 2차원 배열로 변환 (행: 픽셀, 열: RGB)

    # k-means 클러스터링 수행, num_clusters로 클러스터 수 조절
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(pixels)

    # 가장 빈번한 색상 추출
    colors = kmeans.cluster_centers_

    # 정수형 색상으로 변환 후 uint8 타입으로 변환
    colors = colors.round(0).astype(np.uint8)

    # 색상과 그 비율 반환
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    total_count = np.sum(counts)
    color_ratios = [(colors[i], counts[i] / total_count) for i in labels]

    # 색상 비율 큰 순서대로 정렬
    color_ratios_sorted = sorted(color_ratios, key=lambda x: x[1], reverse=True)

    # 클러스터링된 이미지 재구성 및 저장
    clustered_pixels = np.array([colors[label] for label in kmeans.labels_])
    clustered_image = np.reshape(clustered_pixels, (np_image.shape[0], np_image.shape[1], 3))
    plt.imsave(save_path, clustered_image)

    return color_ratios_sorted, save_path


image_path = 'C:/Users/asdfg/source/repos/practice/images/김들내_Sweet sweet girl.jpg'  # 이미지 경로 설정
num_clusters = 10  # 원하는 클러스터 수
top_colors, image_path = extract_top_colors_and_save_clustered_image(image_path, num_clusters)
final = []
for color, ratio in top_colors:
    color_ratio = [color.tolist(), float(round(ratio, 3))]
    final.append(color_ratio)


# 내가 비교하고 싶은 이미지 (예시 데이터)
my_image = final[:5]

# 데이터 표준화 함수
def standardize(values):
    mean = np.mean(values)
    std = np.std(values)
    return [(value - mean) / std for value in values]

# RGB와 비율을 분리하여 표준화
def get_standardized_data(data):
    all_rgb = [rgb for img in data for rgb, _ in img]
    all_ratios = [ratio for img in data for _, ratio in img]

    standardized_rgb = standardize([value for rgb in all_rgb for value in rgb])
    standardized_ratios = standardize(all_ratios)
    
    return standardized_rgb, standardized_ratios

# 주어진 이미지에 대해 표준화된 데이터 반환
def get_standardized_image(image, rgb_mean, rgb_std, ratio_mean, ratio_std):
    standardized_image = []
    for rgb, ratio in image:
        standardized_rgb = [(value - rgb_mean) / rgb_std for value in rgb]
        standardized_ratio = (ratio - ratio_mean) / ratio_std
        standardized_image.append((standardized_rgb, standardized_ratio))
    return standardized_image

# 유클리드 거리 계산 함수
def euclidean_distance(img1, img2):
    distance = 0
    for (rgb1, ratio1), (rgb2, ratio2) in zip(img1, img2):
        distance += np.sum((np.array(rgb1) - np.array(rgb2))**2) + (ratio1 - ratio2)**2
    return np.sqrt(distance)

# 데이터베이스의 RGB와 비율을 표준화
standardized_rgb, standardized_ratios = get_standardized_data(db)

# 평균과 표준 편차 계산
rgb_mean = np.mean(standardized_rgb)
rgb_std = np.std(standardized_rgb)
ratio_mean = np.mean(standardized_ratios)
ratio_std = np.std(standardized_ratios)

# 내 이미지도 표준화
standardized_my_image = get_standardized_image(my_image, rgb_mean, rgb_std, ratio_mean, ratio_std)

# 가장 비슷한 이미지 찾기
min_distance = float('inf')
most_similar_image = None

for image in db:
    standardized_image = get_standardized_image(image, rgb_mean, rgb_std, ratio_mean, ratio_std)
    distance = euclidean_distance(standardized_my_image, standardized_image)
    if distance < min_distance:
        min_distance = distance
        most_similar_image = image

print(f"가장 비슷한 이미지: {most_similar_image}, 거리: {min_distance}")

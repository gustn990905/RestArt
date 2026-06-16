# -*- coding: cp949 -*-



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


image_path = 'C:/Users/asdfg/source/repos/practice/images/김명옥_Utopia.jpg'  # 이미지 경로 설정
num_clusters = 10  # 원하는 클러스터 수
top_colors, image_path = extract_top_colors_and_save_clustered_image(image_path, num_clusters)
final = []
for color, ratio in top_colors:
    color_ratio = [color.tolist(), float(round(ratio, 3))]
    final.append(color_ratio)

print(final)
# -*- coding: cp949 -*-



from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
from sklearn.cluster import SpectralClustering
from scipy.spatial.distance import cdist
import matplotlib.image as mpimg


# 클러스터링 속도용
def resize_image(image_path, base_width=300):
    image = Image.open(image_path)
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = image.resize((base_width, h_size), Image.Resampling.LANCZOS)
    return image

def extract_top_colors_and_save_clustered_image(image_path, num_clusters=3):
    image = resize_image(image_path)
    image = image.convert('RGB')
    np_image = np.array(image)
    pixels = np_image.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_
    colors = colors.round(0).astype(np.uint8)

    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    total_count = np.sum(counts)
    color_ratios = [(colors[i], counts[i] / total_count) for i in labels]

    color_ratios_sorted = sorted(color_ratios, key=lambda x: x[1], reverse=True)

    return color_ratios_sorted

# 'images' 폴더의 모든 파일 경로를 절대 경로 리스트로 가져옵니다.
image_files = [os.path.join('C:/Users/asdfg/source/repos/practice/images', file) for file in os.listdir('C:/Users/asdfg/source/repos/practice/images') if file.endswith(('png', 'jpg', 'jpeg'))]
num = 0
final_dict = {}
for i in range(len(image_files)):
  image_path = image_files[i]
  num_clusters = 10  # 원하는 클러스터 수
  top_colors = extract_top_colors_and_save_clustered_image(image_path, num_clusters)
  final = []
  for color, ratio in top_colors:
      color_ratio = color.tolist()
      final.append(color_ratio)
  final_dict[image_path] = final[0]
  print(num)
  num+=1
  

print(final_dict)

rgb_colors = []
for i in final_dict.values():
  rgb_colors.append(i)

rgb_colors_array = np.array(rgb_colors)

# 유사도 행렬 계산 (가우시안 커널 사용)
def gaussian_kernel(x, y, sigma=1.0):
    return np.exp(-np.linalg.norm(x - y) ** 2 / (2 * (sigma ** 2)))

sigma = 30  # 유사도 분산 하이퍼파라미터
n_samples = len(rgb_colors)
similarity_matrix = np.zeros((n_samples, n_samples))

for i in range(n_samples):
    for j in range(n_samples):
        similarity_matrix[i, j] = gaussian_kernel(rgb_colors_array[i], rgb_colors_array[j], sigma)

# 스펙트럴 클러스터링
n_clusters = 4
spectral = SpectralClustering(n_clusters=n_clusters, affinity='precomputed')
labels = spectral.fit_predict(similarity_matrix)

# 클러스터의 중심 색상 계산
cluster_centers = np.array([rgb_colors_array[labels == i].mean(axis=0) for i in range(n_clusters)], dtype=int)

# 결과 출력
print("선택된 4개의 색상 (RGB):")
print(cluster_centers)

# 시각화
plt.figure(figsize=(8, 2))
for i, color in enumerate(cluster_centers):
    plt.subplot(1, 4, i+1)
    plt.imshow([[color/255]])
    plt.axis('off')
plt.show()

import numpy as np
from scipy.spatial.distance import cdist

# 클러스터 중심과 가장 가까운 색상 찾기
target_keys = []

# rgb_colors_array와 final_dict의 색상 데이터를 이용하여 가장 가까운 값을 찾음
for center in cluster_centers:
    # 모든 색상과 클러스터 중심 간의 거리 계산
    distances = cdist([center], rgb_colors_array, metric='euclidean')[0]

    # 가장 가까운 색상 인덱스 찾기
    closest_index = np.argmin(distances)

    # 가장 가까운 색상에 해당하는 key 찾기
    closest_color = rgb_colors_array[closest_index]
    target_key = [key for key, value in final_dict.items() if np.array_equal(value, closest_color)]

    # 결과에 추가
    target_keys.extend(target_key)

# 결과 출력
print(target_keys)



# 클러스터 중심과 가장 가까운 색상 찾기
target_keys = []

# rgb_colors_array와 final_dict의 색상 데이터를 이용하여 가장 가까운 값을 찾음
for center in cluster_centers:
    # 모든 색상과 클러스터 중심 간의 거리 계산
    distances = cdist([center], rgb_colors_array, metric='euclidean')[0]

    # 가장 가까운 색상 인덱스 찾기
    closest_index = np.argmin(distances)

    # 가장 가까운 색상에 해당하는 key 찾기
    closest_color = rgb_colors_array[closest_index]
    target_key = [key for key, value in final_dict.items() if np.array_equal(value, closest_color)]

    # 결과에 추가
    target_keys.extend(target_key)

# 결과 출력
print(target_keys)


# 최대 4개의 이미지만 출력
# for i in range(min(4, len(target_keys)))
for i in range(len(target_keys)):
    # 이미지 파일 경로를 읽어들임
    image_path = target_keys[i]

    # 이미지 읽기
    image = mpimg.imread(image_path)

    # 이미지 출력
    plt.figure(figsize=(3, 3))
    plt.imshow(image)
    plt.title(target_keys[i])
    plt.show()
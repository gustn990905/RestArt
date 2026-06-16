# -*- coding: utf-8 -*-

"""
RestArt color clustering prototype.

이 파일은 폴더 안의 이미지들을 대상으로 K-means clustering을 수행하여
각 이미지의 대표 색상과 색상 비율을 추출하는 실험 코드이다.

기존 코드에 있던 개인 PC 경로는 제거하고,
실행할 때 --folder-path 옵션으로 이미지 폴더 경로를 입력받도록 정리하였다.
"""

import argparse
import os

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


def extract_top_colors_from_image(image_path, num_clusters=3):
    """
    하나의 이미지에서 대표 색상 cluster를 추출한다.

    Parameters
    ----------
    image_path : str
        분석할 이미지 파일 경로
    num_clusters : int
        추출할 대표 색상 cluster 개수

    Returns
    -------
    list
        [RGB 값, 비율] 형태의 대표 색상 목록
    """

    # 이미지를 열고 RGB 형식으로 변환한다.
    image = Image.open(image_path)
    image = image.convert("RGB")

    # 이미지 픽셀 데이터를 numpy 배열로 변환한다.
    np_image = np.array(image)

    # K-means clustering을 위해 픽셀 배열을 2차원 형태로 변환한다.
    # 예: (height, width, RGB) -> (pixel_count, RGB)
    pixels = np_image.reshape(-1, 3)

    # K-means clustering을 수행한다.
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(pixels)

    # 각 cluster의 중심값을 대표 색상으로 사용한다.
    colors = kmeans.cluster_centers_

    # RGB 값은 정수여야 하므로 반올림 후 uint8 형식으로 변환한다.
    colors = colors.round(0).astype(np.uint8)

    # 각 cluster에 속한 픽셀 개수를 계산한다.
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    total_count = np.sum(counts)

    # 각 대표 색상의 비율을 계산한다.
    color_ratios = [
        (colors[label], counts[index] / total_count)
        for index, label in enumerate(labels)
    ]

    # 비율이 높은 색상부터 정렬한다.
    color_ratios_sorted = sorted(
        color_ratios,
        key=lambda item: item[1],
        reverse=True,
    )

    return color_ratios_sorted


def analyze_images_in_folder(folder_path, num_clusters=10):
    """
    폴더 안의 이미지 파일들을 순회하며 대표 색상을 추출한다.

    Parameters
    ----------
    folder_path : str
        이미지 파일들이 들어 있는 폴더 경로
    num_clusters : int
        이미지별로 추출할 대표 색상 cluster 개수

    Returns
    -------
    dict
        파일명별 대표 색상 분석 결과
    """

    result_dict = {}

    # 폴더 안의 모든 파일을 순회한다.
    for index, filename in enumerate(os.listdir(folder_path)):
        # 이미지 확장자만 분석 대상으로 사용한다.
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(folder_path, filename)

            top_colors = extract_top_colors_from_image(
                image_path=file_path,
                num_clusters=num_clusters,
            )

            # numpy array 형태의 RGB 값을 list로 변환하여 저장한다.
            color_result = []
            for color, ratio in top_colors:
                color_result.append(
                    [
                        color.tolist(),
                        float(round(ratio, 3)),
                    ]
                )

            result_dict[filename] = color_result

        # 실험 진행 상태 확인용 출력
        print(index)

    return result_dict


def main():
    """
    명령행에서 이미지 폴더 경로와 cluster 개수를 입력받아 색상 분석을 실행한다.
    """

    parser = argparse.ArgumentParser(
        description="Extract representative color clusters from images in a folder."
    )

    parser.add_argument(
        "--folder-path",
        required=True,
        help="Path to the image folder to analyze.",
    )

    parser.add_argument(
        "--num-clusters",
        type=int,
        default=10,
        help="Number of color clusters to extract.",
    )

    args = parser.parse_args()

    result = analyze_images_in_folder(
        folder_path=args.folder_path,
        num_clusters=args.num_clusters,
    )

    print(result)


if __name__ == "__main__":
    main()
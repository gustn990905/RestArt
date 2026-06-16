# Color Clustering Prototypes

이 폴더는 RestArt prototype에서 진행한 색상 추출 및 색상 clustering 실험 코드를 정리하기 위한 공간이다.

RestArt의 추천 구조는 사용자 이미지와 작품 이미지에서 대표 색상을 추출하고, 이를 작품 추천, 모바일 리플릿 생성, 색상 취향 설명에 활용한다. 이 폴더는 그 과정에서 사용된 초기 색상 분석 실험과 clustering 기반 prototype 코드를 정리한다.

## 실험 목적

색상 clustering 실험의 목적은 이미지에서 추천에 활용 가능한 대표 색상 정보를 추출하는 것이다.

이미지는 수많은 픽셀 색상으로 구성되어 있기 때문에, 추천 로직에서 바로 사용하기 어렵다. 따라서 주요 색상 cluster를 추출하고, 대표 RGB 값과 색상 비율을 계산하여 추천 기준으로 변환한다.

## 관련 기능

이 실험은 RestArt의 다음 기능과 연결된다.

- 공간 기반 작품 추천
- 모바일 리플릿 생성
- 색상 기반 작품 추천
- 작품 이미지 색상 분석
- 사용자 이미지 색상 분석
- RestArt 색상 dictionary 매칭
- 리플릿 디자인 타입 선택

## 관련 source

이 폴더는 다음 source와 연결된다.

- tools/recommendation-model/color_extraction/kmeans_color_extractor.py
- tools/recommendation-model/color_dictionary/restart_color_map.py
- tools/recommendation-model/color_dictionary/color_description_dictionary.py
- tools/recommendation-model/prototype/image_utils.py
- docs/14-ai-experiments/color-analysis-summary.md

## 실험 흐름

색상 clustering 실험은 다음 흐름으로 정리할 수 있다.

1. 이미지 입력
2. 이미지 픽셀 데이터 추출
3. 색상 clustering 수행
4. 대표 색상 RGB 값 계산
5. 색상 cluster 비율 계산
6. RestArt 색상 dictionary와 매칭
7. 추천 로직 또는 리플릿 디자인 로직에 활용

## K-means 기반 색상 추출

RestArt prototype에서는 K-means 기반 색상 추출 방식을 사용한다.

K-means는 이미지의 픽셀 색상들을 여러 cluster로 나누고, 각 cluster의 중심값을 대표 색상으로 사용할 수 있게 한다.

이 방식은 다음 정보를 얻는 데 활용된다.

- 대표 색상
- 색상 cluster 개수
- 색상 cluster 비율
- 이미지의 전체적인 색상 분위기
- 작품 이미지와 사용자 이미지 사이의 색상 비교 기준

## Spectral color experiment

색상 분석 과정에서는 spectral clustering 또는 spectral image processing 방식도 실험적으로 사용될 수 있다.

이 실험은 이미지 색상 구조를 다른 방식으로 분류하거나, 색상 기반 추천 기준을 보완하기 위한 prototype 성격을 가진다.

현재 repository에서는 production-ready module이 아니라, 색상 기반 추천 구조를 검토한 실험 코드로 정리한다.

## RestArt 색상 dictionary와의 연결

색상 clustering 결과는 RGB 값 형태로 도출된다.

이 RGB 값은 RestArt 색상 dictionary와 비교되어 색상 이름, 색상 그룹, 색상 설명으로 변환될 수 있다.

관련 파일은 다음과 같다.

- tools/recommendation-model/color_dictionary/restart_color_map.py
- tools/recommendation-model/color_dictionary/color_description_dictionary.py

이를 통해 이미지 색상 분석 결과는 단순 수치 데이터가 아니라 추천 설명과 연결되는 데이터가 된다.

## 활용 예시

색상 clustering 실험 결과는 다음 방식으로 활용될 수 있다.

- 공간 이미지의 대표 색상 추출
- 작품 이미지의 대표 색상 추출
- 사용자 이미지와 작품 이미지의 색상 유사도 판단
- 모바일 리플릿의 대표 색상 결정
- 리플릿 디자인 타입 선택
- 사용자 색상 취향 설명 생성

## 포함 기준

이 폴더에는 공개 가능한 실험 코드만 포함한다.

포함 가능한 항목은 다음과 같다.

- 색상 추출 실험 코드
- K-means clustering code
- spectral color experiment code
- 색상 비교 utility code
- 실험 README

## 제외 기준

이 폴더에는 다음 항목을 포함하지 않는다.

- DB password
- API key
- private token
- 내부 서버 정보
- 민감한 원본 이미지 데이터
- 자동 생성 cache
- 실행 환경별 임시 파일
- 원본 기획 문서 또는 내부 문서

## 구현 범위

이 폴더는 RestArt 추천 구조에서 색상 분석이 어떻게 실험되고 prototype화되었는지 보여주는 목적을 가진다.

최종 서비스 코드와 실험 코드를 구분하기 위해, 안정적으로 정리된 색상 추출 module은 `tools/recommendation-model/color_extraction/`에 두고, 초기 실험 코드는 이 폴더에 분리하여 정리한다.

## 관련 문서

- docs/14-ai-experiments/color-analysis-summary.md
- docs/14-ai-experiments/recommendation-algorithm-summary.md
- docs/06-architecture/color-extraction-pipeline.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md

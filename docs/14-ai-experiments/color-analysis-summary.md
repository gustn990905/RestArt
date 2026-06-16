# 색상 분석 요약

이 문서는 RestArt prototype에서 사용한 색상 분석 구조를 정리한다.

RestArt의 색상 분석은 사용자 이미지 또는 작품 이미지에서 대표 색상을 추출하고, 이를 RestArt 색상 체계와 연결하여 작품 추천, 모바일 리플릿 생성, 색상 취향 설명에 활용하는 기능이다.

## 기능 목적

색상 분석 기능의 목적은 이미지에서 추출된 색상 정보를 추천 가능한 데이터로 변환하는 것이다.

이미지의 RGB 값만으로는 사용자의 취향이나 작품 추천 기준을 설명하기 어렵기 때문에, RestArt는 대표 색상 추출 결과를 색상 이름, 색상 그룹, 색상 설명과 연결한다.

## 관련 source

- tools/recommendation-model/color_extraction/kmeans_color_extractor.py
- tools/recommendation-model/color_dictionary/restart_color_map.py
- tools/recommendation-model/color_dictionary/color_description_dictionary.py
- tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
- tools/recommendation-model/prototype/image_utils.py

## 관련 문서

- docs/06-architecture/color-extraction-pipeline.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md
- docs/14-ai-experiments/emotion-and-color-table-summary.md

## 색상 분석의 전체 흐름

RestArt의 색상 분석은 다음 순서로 정리할 수 있다.

1. 사용자 이미지 또는 작품 이미지 입력
2. 이미지에서 대표 색상 추출
3. 대표 RGB 값 계산
4. RestArt 색상 체계와 비교
5. 가장 가까운 색상 이름 또는 색상 그룹 선택
6. 색상 설명 dictionary와 연결
7. 작품 추천 또는 리플릿 디자인 선택에 활용

## 1. 이미지 입력

색상 분석의 입력은 사용자 이미지 또는 작품 이미지다.

입력 이미지는 다음 기능에서 사용될 수 있다.

- 공간 기반 작품 추천
- 모바일 리플릿 생성
- 작품 이미지 분석
- 색상 기반 추천 후보 선정

## 2. 대표 색상 추출

대표 색상 추출은 이미지 안에서 주요 색상을 찾아내는 과정이다.

RestArt prototype에서는 K-means 기반 색상 추출 로직이 사용되며, 이미지의 픽셀 정보를 기준으로 색상 cluster를 생성한다.

관련 source:

- tools/recommendation-model/color_extraction/kmeans_color_extractor.py

대표 색상 추출 결과는 이후 추천 로직에서 색상 비교 기준으로 사용된다.

## 3. RGB 값 계산

추출된 대표 색상은 RGB 값으로 표현된다.

RGB 값은 색상 비교를 위한 수치 데이터로 사용되며, RestArt 색상 dictionary와의 거리 계산 또는 색상 매칭에 활용된다.

예시 구조:

- 대표 색상 이름
- 대표 RGB 값
- 색상 cluster 비율
- 색상 cluster 개수

## 4. RestArt 색상 체계와 매칭

이미지에서 추출한 RGB 값은 RestArt 색상 체계와 비교된다.

관련 source:

- tools/recommendation-model/color_dictionary/restart_color_map.py

이 파일은 RestArt에서 사용하는 색상 이름과 대표 RGB 값을 정리한다.

색상 매칭의 목적은 다음과 같다.

- RGB 값을 의미 있는 색상 이름으로 변환
- 사용자 이미지와 작품 이미지의 색상 연결
- 작품 추천 기준 생성
- 리플릿 디자인 선택 기준 생성

## 5. 색상 설명 dictionary 연결

색상 이름이 결정되면 색상 설명 dictionary와 연결할 수 있다.

관련 source:

- tools/recommendation-model/color_dictionary/color_description_dictionary.py

색상 설명 dictionary는 색상 이름, 대표 RGB 값, 사용자 취향 설명 문장을 포함한다.

이 정보는 추천 결과를 단순 이미지 목록이 아니라, 사용자가 이해할 수 있는 설명형 결과로 변환하는 데 사용될 수 있다.

## 6. 작품 추천과의 연결

색상 분석 결과는 작품 추천에서 중요한 기준으로 사용된다.

공간 기반 작품 추천에서는 사용자의 공간 이미지에서 추출된 색상과 작품 데이터의 색상 정보를 비교한다.

모바일 리플릿 생성에서는 전시장 또는 작품 이미지에서 추출된 대표 색상을 바탕으로 리플릿 결과와 추천 작품을 구성한다.

색상 기반 추천의 역할은 다음과 같다.

- 사용자 이미지와 시각적으로 어울리는 작품 추천
- 작품 데이터의 색상 cluster와 사용자 이미지 색상 비교
- 색상 취향을 반영한 추천 결과 구성
- 추천 결과의 설명 가능성 강화

## 7. 모바일 리플릿과의 연결

모바일 리플릿 생성 기능에서는 색상 분석 결과가 리플릿 디자인 타입 결정에도 활용된다.

대표 색상, 색상 그룹, signature color 정보는 리플릿의 시각적 방향성을 정하는 기준이 된다.

관련 source:

- tools/recommendation-model/leaflet_generation/leaflet_image_selector.py

리플릿 기능에서 색상 분석은 다음 역할을 한다.

- 대표 이미지의 색상 분석
- 사용자 색상 정보 생성
- 추천 작품 색상 기준 생성
- 리플릿 디자인 타입 선택

## 8. 공간 기반 작품 추천과의 연결

공간 기반 작품 추천에서는 공간 이미지의 색상과 분위기를 분석하여 공간에 어울리는 작품을 추천한다.

이때 색상 분석은 공간의 시각적 특성을 정량화하는 역할을 한다.

색상 분석 결과는 감성 분석 결과와 함께 사용될 수 있으며, 이를 통해 단순 색상 유사도뿐 아니라 공간의 분위기와 어울리는 작품 추천이 가능해진다.

## 구현 범위

현재 repository는 기존 prototype에서 사용된 색상 추출 코드와 색상 dictionary를 공개 가능한 형태로 정리한다.

원본 색상 문서나 내부 기획 자료는 포함하지 않고, 추천 로직에 필요한 색상 구조와 기능 흐름만 문서화한다.

## 정리 기준

이 문서와 관련 source는 다음 기준으로 정리되었다.

- 기존 prototype의 색상 분석 흐름 유지
- 색상 dictionary를 코드 형태로 정리
- 공개 가능한 색상명과 RGB 값만 포함
- 민감한 원본 문서와 내부 자료는 제외
- 추천 로직에서의 역할 중심으로 설명

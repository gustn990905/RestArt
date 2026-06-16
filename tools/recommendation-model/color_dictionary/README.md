# RestArt 색상 Dictionary

이 폴더는 RestArt 추천 로직에서 사용하는 색상 dictionary와 색상 설명 구조를 정리한다.

RestArt의 색상 기반 추천은 사용자 이미지 또는 작품 이미지에서 추출된 대표 색상을 기준으로, 사전에 정의된 색상 체계와 매칭하여 추천 기준을 만든다.

## 기능 역할

색상 dictionary는 다음 기능에서 사용된다.

- 공간 기반 작품 추천
- 모바일 리플릿 생성
- 색상 기반 작품 추천
- 사용자 취향 색상 설명
- 작품 이미지와 사용자 이미지의 색상 연결
- 리플릿 디자인 타입 선택

## 관련 source

이 폴더는 기존 RestArt prototype에서 사용된 색상 관련 자료를 정리한 것이다.

관련 기능은 다음 파일들과 연결된다.

- tools/recommendation-model/color_extraction/kmeans_color_extractor.py
- tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
- tools/recommendation-model/prototype/image_utils.py
- docs/06-architecture/color-extraction-pipeline.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md

## 색상 체계의 역할

RestArt 색상 체계는 이미지에서 추출된 RGB 값을 단순 수치로만 사용하지 않고, 의미 있는 색상 이름과 설명으로 변환하기 위한 기준이다.

예를 들어 사용자 이미지에서 특정 대표 색상이 추출되면, 이 색상은 RestArt 색상 dictionary를 통해 다음 정보와 연결될 수 있다.

- 색상 이름
- 대표 RGB 값
- 색상 설명
- 사용자 취향 설명
- 추천 작품과의 색상 연결 기준

## 추천 흐름에서의 사용 방식

색상 dictionary는 다음 흐름에서 사용된다.

1. 사용자 이미지 또는 작품 이미지 입력
2. K-means 또는 색상 추출 로직으로 대표 색상 추출
3. 추출된 RGB 값을 RestArt 색상 체계와 비교
4. 가장 가까운 색상 이름 또는 색상 그룹 선택
5. 색상 설명 또는 취향 설명 생성
6. 작품 추천 또는 리플릿 디자인 선택에 반영

## 데이터 구성 방향

이 폴더에는 공개 가능한 색상 dictionary 코드만 포함한다.

원본 문서나 내부 기획 자료를 그대로 포함하지 않고, 추천 로직에 필요한 색상 구조만 정리한다.

구성 예정 파일은 다음과 같다.

- restart_color_map.py
- color_description_dictionary.py

## restart_color_map.py

`restart_color_map.py`는 RestArt 색상 이름과 대표 RGB 값을 정리하는 코드 파일이다.

이 파일은 색상 분석 결과를 색상 이름으로 변환하는 기준으로 사용된다.

## color_description_dictionary.py

`color_description_dictionary.py`는 색상 이름별 설명 문구를 정리하는 코드 파일이다.

이 파일은 사용자 취향 설명, 추천 결과 설명, 리플릿 결과 설명 등에 활용될 수 있다.

## 구현 범위

현재 repository에서는 기존 prototype과 색상 자료를 바탕으로 공개 가능한 색상 dictionary 구조를 정리한다.

민감한 원본 문서, 내부 데이터 전체, 비공개 기획 자료는 포함하지 않는다.

또한 실행 안정성을 위해 원본 코드에서 불필요하거나 중복된 구조는 정리된 형태로 반영한다.

## 관련 문서

- docs/14-ai-experiments/color-analysis-summary.md
- docs/14-ai-experiments/emotion-and-color-table-summary.md
- docs/06-architecture/color-extraction-pipeline.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md

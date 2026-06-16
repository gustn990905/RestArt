# 추천 알고리즘 요약

이 문서는 RestArt prototype의 추천 알고리즘 구조를 요약한다.

RestArt의 추천 알고리즘은 사용자 이미지, 공간 이미지, 전시 이미지, 작품 이미지에서 색상 정보와 감성 정보를 추출하고, 이를 작품 데이터와 비교하여 추천 결과를 구성하는 구조를 가진다.

## 추천 알고리즘의 목적

RestArt 추천 알고리즘의 목적은 단순히 작품 이미지를 나열하는 것이 아니라, 사용자 입력 이미지와 작품 데이터 사이의 시각적·감성적 관계를 분석하여 적합한 작품과 전시 경험을 연결하는 것이다.

추천 알고리즘은 다음 기능과 연결된다.

- 공간 기반 작품 추천
- 모바일 리플릿 생성
- 색상 기반 작품 추천
- 감성 기반 작품 추천
- 전시 추천
- AR 작품 배치와의 연결 가능성

## 관련 source

- tools/recommendation-model/prototype/image_utils.py
- tools/recommendation-model/color_extraction/kmeans_color_extractor.py
- tools/recommendation-model/color_dictionary/restart_color_map.py
- tools/recommendation-model/color_dictionary/color_description_dictionary.py
- tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
- tools/image_matching/
- apps/backend/api-prototype/recommend_picture.py
- apps/backend/api-prototype/signature_color.py
- apps/backend/api-prototype/spectral_image.py
- apps/backend/api-prototype/main.py

## 관련 문서

- docs/06-architecture/ai-recommendation-architecture.md
- docs/06-architecture/color-extraction-pipeline.md
- docs/06-architecture/emotion-mapping-pipeline.md
- docs/06-architecture/similarity-ranking-logic.md
- docs/14-ai-experiments/color-analysis-summary.md
- docs/14-ai-experiments/emotion-and-color-table-summary.md
- docs/14-ai-experiments/multimodal-emotion-extraction.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md

## 전체 추천 구조

RestArt의 추천 구조는 다음 단계로 정리할 수 있다.

1. 사용자 입력 이미지 또는 공간 이미지 수집
2. 이미지 색상 분석
3. 대표 색상 및 색상 cluster 추출
4. RestArt 색상 dictionary와 매칭
5. 이미지 또는 텍스트 기반 감성 정보 추론
6. 작품 데이터의 색상 및 감성 정보와 비교
7. 이미지 매칭 또는 유사도 기반 후보 선정
8. 추천 작품 구성
9. 전시 정보 또는 리플릿 결과와 연결
10. 웹, 모바일, AR 기능으로 확장

## 1. 사용자 입력 데이터

추천 알고리즘의 입력은 기능에 따라 달라진다.

공간 기반 작품 추천에서는 공간, 인테리어, 장소 이미지가 입력된다.

모바일 리플릿 생성에서는 전시장 또는 작품 관련 이미지가 입력된다.

전시 추천에서는 사용자 위치 정보 또는 리플릿 결과에서 연결되는 전시 후보 정보가 사용된다.

## 2. 색상 분석

색상 분석은 이미지의 시각적 특성을 추출하는 단계다.

RestArt prototype에서는 K-means 기반 색상 추출 로직과 색상 dictionary를 사용하여 이미지에서 대표 색상을 추출하고, 이를 색상 이름 및 설명과 연결한다.

색상 분석 결과는 다음 기능에서 사용된다.

- 작품 색상 비교
- 공간 이미지와 작품 이미지의 색상 매칭
- 모바일 리플릿의 대표 색상 결정
- 리플릿 디자인 타입 선택
- 사용자 색상 취향 설명 생성

## 3. RestArt 색상 dictionary

RestArt 색상 dictionary는 추출된 RGB 값을 의미 있는 색상 이름과 설명으로 변환하기 위한 기준이다.

관련 source는 다음과 같다.

- tools/recommendation-model/color_dictionary/restart_color_map.py
- tools/recommendation-model/color_dictionary/color_description_dictionary.py

이 구조는 이미지 분석 결과를 추천 결과 설명으로 확장하는 역할을 한다.

## 4. 감성 정보 활용

감성 정보는 작품 또는 이미지가 가진 분위기와 정서적 특성을 설명한다.

RestArt 추천 구조에서는 감성 정보가 다음 방식으로 활용된다.

- 작품 감성 태그와 사용자 이미지 감성 비교
- 공간 이미지 분위기와 작품 분위기 연결
- 모바일 리플릿에서 감성 기반 추천 작품 구성
- 색상 기반 추천 결과의 보완 기준 제공

감성 정보는 수동으로 정리된 감성 데이터뿐 아니라, LLaVA 기반 multimodal experiment와도 연결될 수 있다.

## 5. 이미지 매칭

이미지 매칭은 사용자 입력 이미지와 작품 후보 이미지 사이의 시각적 관련성을 비교하는 단계다.

관련 source는 다음과 같다.

- tools/image_matching/image_loader.py
- tools/image_matching/image_preprocessing.py
- tools/image_matching/similarity.py
- tools/image_matching/feature_matcher.py
- tools/image_matching/matching_service.py

이미지 매칭은 모바일 리플릿 생성 기능에서 특히 중요하다.

사용자가 입력한 전시장 또는 작품 이미지와 후보 작품 이미지를 비교하여, 리플릿 결과에 사용할 대표 이미지와 추천 후보를 찾는다.

## 6. 공간 기반 작품 추천

공간 기반 작품 추천은 사용자의 공간 이미지에 어울리는 작품을 찾는 기능이다.

처리 흐름은 다음과 같다.

1. 공간 이미지 입력
2. 색상 또는 분위기 분석
3. 텍스트 설명 또는 감성 정보 결합
4. 공간 감성 또는 대표 색상 도출
5. 작품 데이터의 색상 및 감성 정보와 비교
6. 공간에 어울리는 추천 작품 반환

이 흐름은 `/find_emotion_interior/` endpoint와 연결된다.

## 7. 모바일 리플릿 추천

모바일 리플릿 추천은 전시장 또는 작품 이미지 입력을 기반으로 개인화된 리플릿 결과를 생성하는 기능이다.

처리 흐름은 다음과 같다.

1. 사용자 이미지 입력
2. 작품 후보 이미지 매칭
3. 대표 이미지 선정
4. 대표 색상 추출
5. 색상 기반 추천 작품 선정
6. 감성 기반 추천 작품 선정
7. 추천 전시 정보 연결
8. 리플릿 디자인 타입 결정
9. 리플릿 결과 반환

이 흐름은 `/leaflet_creating/` endpoint와 연결된다.

## 8. 전시 추천과의 연결

RestArt의 추천 알고리즘은 작품 추천에서 끝나지 않고 전시 추천으로 확장된다.

전시 추천은 두 가지 방식으로 연결된다.

- 사용자 위치를 기준으로 가까운 전시 추천
- 모바일 리플릿 결과 안에 추천 전시 정보 연결

이를 통해 추천 결과가 실제 전시 탐색과 관람 경험으로 이어질 수 있다.

## 9. 추천 결과의 활용

추천 결과는 다음 기능으로 확장될 수 있다.

- 웹 화면의 작품 추천 결과
- 모바일 리플릿 결과
- 전시 추천 결과
- 사용자 색상 취향 설명
- AR 작품 배치 기능
- 작품 상세 페이지 또는 작가 정보 연결

## 구현 범위

현재 repository는 기존 prototype의 추천 알고리즘을 공개 가능한 코드와 문서 중심으로 정리한다.

원본 사업 문서, 내부 기획 문서, 전체 원본 감성 데이터, 민감한 DB 정보는 포함하지 않는다.

추천 알고리즘은 production-ready service라기보다, RestArt prototype에서 구현하고 실험한 색상·감성·이미지 기반 추천 구조를 정리한 것이다.

## 정리 기준

이 문서는 다음 기준으로 작성되었다.

- 기존 prototype의 추천 흐름을 유지
- 색상 분석, 감성 정보, 이미지 매칭을 분리해 설명
- 모바일 리플릿과 공간 기반 작품 추천의 차이를 명확히 정리
- 원본 데이터 전체가 아니라 공개 가능한 구조만 요약
- 추천 알고리즘이 RestArt 전체 서비스 안에서 어떤 역할을 하는지 설명

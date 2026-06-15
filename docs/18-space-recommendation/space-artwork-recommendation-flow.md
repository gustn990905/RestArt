# 공간 기반 작품 추천 흐름

이 문서는 RestArt backend prototype의 공간 기반 작품 추천 기능을 정리한다.

공간 기반 작품 추천 기능은 사용자가 공간, 인테리어, 장소 이미지를 입력했을 때 해당 공간의 색상, 분위기, 감성 정보를 분석하고, 그 결과를 작품 데이터와 비교하여 공간에 어울리는 작품을 추천하는 기능이다.

## 기능 목적

공간 기반 작품 추천은 사용자가 가진 공간의 분위기와 어울리는 작품을 찾기 위한 기능이다.

모바일 리플릿 기능이 전시장 또는 작품 이미지 기반의 개인화 리플릿을 생성하는 기능이라면, 공간 기반 작품 추천은 사용자의 실제 공간 이미지에 어울리는 작품을 추천하는 기능이다.

## 관련 endpoint

POST /find_emotion_interior/

## 관련 source

- apps/backend/api-prototype/main.py
- apps/backend/api-prototype/recommend_picture.py
- apps/backend/api-prototype/signature_color.py
- apps/backend/api-prototype/spectral_image.py
- apps/backend/api-prototype/schemas/recommendation_schema.py
- tools/recommendation-model/

## 모바일 리플릿 기능과의 차이

| 구분          | 모바일 리플릿 생성                               | 공간 기반 작품 추천                              |
| ------------- | ------------------------------------------------ | ------------------------------------------------ |
| 입력          | 전시장 또는 작품 이미지                          | 공간, 인테리어, 장소 이미지                      |
| 목적          | 개인화 리플릿 생성                               | 공간에 어울리는 작품 추천                        |
| 핵심 기준     | 이미지 매칭, 대표 색상, 추천 작품, 리플릿 디자인 | 공간 이미지 분석, 감성 예측, 작품 감성/색상 비교 |
| 결과          | 리플릿 결과 구조                                 | 추천 작품 결과                                   |
| 관련 endpoint | POST /leaflet_creating/                          | POST /find_emotion_interior/                     |

## 전체 처리 흐름

1. 공간 또는 인테리어 이미지 입력
2. 이미지 특징 분석
3. 텍스트 설명 또는 분위기 정보 결합
4. 감성 또는 분위기 예측
5. 작품 DB의 감성 및 색상 정보와 비교
6. 추천 작품 후보 선정
7. 추천 결과 반환

## 1. 공간 또는 인테리어 이미지 입력

사용자는 추천을 받고 싶은 공간, 인테리어, 장소 이미지를 입력한다.

이 이미지는 공간의 색상, 밝기, 분위기, 시각적 특징을 분석하기 위한 기준 데이터로 사용된다.

backend prototype에서는 `/find_emotion_interior/` endpoint가 이 입력을 처리한다.

## 2. 이미지 특징 분석

입력된 공간 이미지는 색상, 시각적 특징, 분위기 분석의 대상이 된다.

이 단계에서는 공간 이미지에서 대표 색상 또는 시각적 특성을 추출하고, 이후 추천 기준으로 사용할 수 있는 형태로 변환한다.

관련 코드에는 색상 분석, signature color 추출, spectral image processing과 관련된 prototype source가 포함된다.

## 3. 텍스트 설명 또는 분위기 정보 결합

공간 추천 흐름은 이미지 정보만 사용하는 것이 아니라, 공간에 대한 설명이나 분위기 관련 텍스트 정보를 함께 사용할 수 있다.

이를 통해 단순히 색상이 유사한 작품뿐만 아니라, 공간의 감성적 방향과 어울리는 작품을 추천할 수 있다.

## 4. 감성 또는 분위기 예측

이미지와 텍스트 정보를 바탕으로 공간의 감성 또는 분위기 정보를 예측한다.

예측된 감성 정보는 작품 DB의 감성 태그 또는 분위기 정보와 비교된다.

이 단계는 RestArt의 작품 추천이 단순 이미지 검색이 아니라, 공간과 작품 사이의 감성적 적합성을 고려하는 추천 구조임을 보여준다.

## 5. 작품 DB의 감성 및 색상 정보와 비교

예측된 공간 감성, 대표 색상, 분위기 정보는 작품 DB에 저장된 작품 정보와 비교된다.

비교 기준은 다음과 같다.

- 작품 색상 정보
- 작품 감성 태그
- 작품 설명 정보
- 작품 이미지 기반 특징
- 공간 이미지의 대표 색상 또는 분위기

이 과정을 통해 공간에 어울리는 작품 후보를 찾는다.

## 6. 추천 작품 후보 선정

시스템은 공간 분석 결과와 작품 데이터의 유사성을 기준으로 추천 작품 후보를 선정한다.

추천 결과는 사용자가 자신의 공간에 배치하거나 감상할 수 있는 작품 후보로 활용된다.

## 7. 추천 결과 반환

최종적으로 backend는 공간 이미지 분석 결과와 매칭된 추천 작품 정보를 반환한다.

이 결과는 웹 또는 모바일 화면에서 작품 추천 결과로 표현될 수 있으며, 이후 AR 작품 배치 기능과도 연결될 수 있다.

## 관련 기능 연결

공간 기반 작품 추천은 RestArt의 여러 기능과 연결된다.

- AI 색상 분석
- 감성 기반 작품 추천
- 작품 DB
- 웹/모바일 추천 결과 화면
- AR 작품 배치
- 이미지 기반 추천 pipeline

## 구현 범위

현재 repository에서는 기존 backend prototype의 `/find_emotion_interior/` 흐름을 기준으로 공간 기반 작품 추천 기능을 문서화한다.

일부 image processing 또는 emotion prediction helper는 기존 prototype 내부 또는 실험 코드와 연결될 수 있으며, 최종 repository에서는 공개 가능한 코드와 문서 중심으로 정리한다.

민감한 원본 데이터, 내부 DB 값, 비공개 기획 문서는 포함하지 않는다.

## 관련 문서

- apps/backend/api-prototype/README.md
- docs/06-architecture/ai-recommendation-architecture.md
- docs/06-architecture/color-extraction-pipeline.md
- docs/06-architecture/emotion-mapping-pipeline.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/10-image-matching/image-matching-flow.md

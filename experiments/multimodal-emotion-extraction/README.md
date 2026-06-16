# Multimodal Emotion Extraction Experiment

이 폴더는 RestArt prototype에서 이미지 기반 감성 추출 가능성을 실험한 LLaVA 기반 multimodal AI 실험을 정리한다.

이 실험은 작품 이미지 또는 사용자 입력 이미지에서 감성 후보를 추론하고, 해당 감성 정보를 작품 추천 로직과 연결할 수 있는지 검토하기 위한 실험이다.

## 실험 목적

RestArt의 추천 구조는 색상 정보뿐 아니라 감성 정보를 함께 활용한다.

색상 정보는 이미지의 시각적 특성을 설명하고, 감성 정보는 이미지가 전달하는 분위기와 정서적 인상을 설명한다.

LLaVA 기반 감성 추출 실험의 목적은 다음과 같다.

- 이미지에서 감성 후보를 추론할 수 있는지 확인
- 작품 이미지와 감성 태그 사이의 연결 가능성 검토
- 공간 이미지 또는 작품 이미지의 분위기를 추천 로직에 반영
- 색상 기반 추천을 감성 기반 추천으로 보완
- 향후 multimodal recommendation pipeline의 실험 근거 확보

## 관련 notebook

이 폴더에는 다음 notebook을 정리할 예정이다.

- LLava_3.ipynb

해당 notebook은 LLaVA 계열 multimodal model을 활용하여 이미지 입력과 텍스트 prompt를 함께 처리하는 실험 코드다.

## 실험 흐름

LLaVA 기반 감성 추출 실험은 다음 흐름으로 정리할 수 있다.

1. 이미지 입력
2. 감성 후보 또는 감성 분류 prompt 구성
3. multimodal model에 이미지와 prompt 입력
4. 이미지에 가장 가까운 감성 또는 분위기 추론
5. 추론 결과를 감성 태그 또는 추천 기준으로 변환
6. 작품 추천, 공간 기반 작품 추천, 모바일 리플릿 추천과 연결 가능성 검토

## RestArt 추천 구조와의 연결

이 실험은 RestArt의 다음 기능과 연결된다.

- 공간 기반 작품 추천
- 감성 기반 작품 추천
- 작품 이미지 감성 태그 생성
- 사용자 이미지 분위기 분석
- 모바일 리플릿의 감성 기반 추천 작품 선정
- 색상 분석 결과의 보완 기준

## 색상 분석과의 차이

색상 분석은 이미지의 대표 색상, RGB 값, 색상 cluster를 중심으로 작동한다.

반면 감성 추출은 이미지가 주는 분위기, 정서, 인상에 집중한다.

두 분석 방식은 다음과 같이 구분된다.

| 구분      | 색상 분석                     | 감성 추출                        |
| --------- | ----------------------------- | -------------------------------- |
| 입력      | 이미지 픽셀, RGB 값           | 이미지, 텍스트 prompt            |
| 기준      | 대표 색상, 색상 cluster       | 분위기, 감성 후보, 이미지 인상   |
| 결과      | 색상명, RGB, 색상 그룹        | 감성 태그, 분위기 분류           |
| 활용      | 색상 기반 작품 추천           | 감성 기반 작품 추천              |
| 연결 기능 | 리플릿 디자인, 색상 취향 설명 | 작품 분위기 추천, 공간 감성 추천 |

## 실험 범위

이 폴더의 notebook은 prototype 수준의 실험 코드로 정리한다.

즉, 현재 repository에서 이 실험은 production-ready AI service가 아니라, RestArt 추천 구조에 감성 추출을 적용할 수 있는지 확인한 실험 근거로 사용된다.

## 포함하지 않는 것

이 repository에는 다음 항목을 포함하지 않는다.

- 비공개 API key
- model access token
- private dataset
- 민감한 원본 이미지 데이터
- 내부 기획 문서 원본
- 실행 환경에 따라 자동 생성되는 cache 또는 output 파일

## 향후 확장 가능성

이 실험은 다음 방향으로 확장될 수 있다.

- 작품 이미지별 감성 태그 자동 생성
- 공간 이미지의 분위기 자동 분석
- 색상 기반 추천과 감성 기반 추천의 가중치 결합
- LLM 또는 multimodal model 기반 작품 설명 생성
- 개인화 추천 결과의 설명 문장 생성

## 관련 문서

- docs/14-ai-experiments/multimodal-emotion-extraction.md
- docs/14-ai-experiments/emotion-and-color-table-summary.md
- docs/14-ai-experiments/color-analysis-summary.md
- docs/06-architecture/emotion-mapping-pipeline.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md

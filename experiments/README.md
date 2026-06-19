# RestArt Experiments

이 폴더는 RestArt 프로젝트에서 사용한 색상 분석, 이미지 clustering, 멀티모달 감성 추출 관련 실험 자산을 정리한 공간이다.

`experiments/`는 실제 서비스 실행 코드보다 실험 검증과 기능 가능성 확인에 가까운 자료를 관리한다. 검증된 로직은 이후 `tools/`, `apps/`, `docs/`의 기능 구조와 연결될 수 있다.

## Experiments Structure

```text
experiments/
├─ color-clustering-prototypes/
└─ multimodal-emotion-extraction/
```

## Folder Overview

| Folder                           | Role                    | Description                                                                 |
| -------------------------------- | ----------------------- | --------------------------------------------------------------------------- |
| `color-clustering-prototypes/`   | 색상 clustering 실험    | 이미지에서 대표 색상을 추출하고 clustering 방식으로 색상 특성을 분석한 실험 |
| `multimodal-emotion-extraction/` | 멀티모달 감성 추출 실험 | 이미지와 텍스트 정보를 바탕으로 작품의 감성 정보를 추출하는 실험            |

## color-clustering-prototypes

```text
experiments/color-clustering-prototypes/
├─ src/
└─ README.md
```

`color-clustering-prototypes/`는 이미지 기반 색상 분석 기능을 검토하기 위한 실험 폴더이다.

주요 목적은 다음과 같다.

- 이미지에서 대표 색상 추출
- 색상 clustering 방식 검토
- 작품 이미지와 공간 이미지의 색상 특성 비교
- 추천 모델에서 사용할 색상 기반 feature 구조 검토
- 색상 분석 결과를 추천 logic과 연결할 수 있는지 확인

이 실험은 RestArt의 공간 기반 작품 추천 기능과 직접 연결된다. 사용자가 업로드한 공간 이미지의 색상 특성을 추출하고, 작품 데이터의 색상 정보와 비교하여 어울리는 작품을 추천하는 흐름의 기반이 된다.

세부 내용은 다음 문서를 기준으로 확인한다.

```text
experiments/color-clustering-prototypes/README.md
```

## multimodal-emotion-extraction

```text
experiments/multimodal-emotion-extraction/
├─ LLava_3.ipynb
└─ README.md
```

`multimodal-emotion-extraction/`은 작품 이미지와 설명 정보를 함께 활용하여 감성 정보를 추출하는 실험 폴더이다.

주요 목적은 다음과 같다.

- 작품 이미지 기반 감성 추출 가능성 검토
- 작품 설명과 이미지 정보를 함께 사용하는 분석 흐름 검토
- 색상 정보와 감성 정보의 연결 가능성 확인
- 작품 추천에서 감성 기준을 활용할 수 있는지 확인
- 전시 리플릿 생성 시 작품별 설명과 분위기 정보를 자동화할 수 있는지 검토

포함된 notebook은 실험 흐름을 확인하기 위한 자료이며, 정식 서비스 실행 module이라기보다 분석 가능성을 검토한 실험 자산으로 관리한다.

세부 내용은 다음 문서를 기준으로 확인한다.

```text
experiments/multimodal-emotion-extraction/README.md
```

## Relationship with Main Project

`experiments/`의 실험 결과는 RestArt의 주요 기능과 다음과 같이 연결된다.

| Experiment Area       | Related Feature               |
| --------------------- | ----------------------------- |
| 색상 clustering       | 공간 이미지 기반 작품 추천    |
| 대표 색상 추출        | 작품 색상 사전 및 색상명 변환 |
| 이미지 기반 감성 추출 | 감성 기반 작품 추천           |
| 멀티모달 분석         | 작품 설명 생성 및 리플릿 구성 |
| 색상·감성 연결        | 추천 ranking logic 고도화     |

## Related Folders

| Folder                                         | Connection                          |
| ---------------------------------------------- | ----------------------------------- |
| `tools/recommendation-model/`                  | 추천 모델과 색상·유사도 계산 도구   |
| `tools/recommendation-model/color_extraction/` | 색상 추출 module                    |
| `tools/recommendation-model/color_dictionary/` | 색상 사전 및 색상명 변환            |
| `tools/recommendation-model/similarity/`       | 유사도 계산 logic                   |
| `tools/image_matching/`                        | 이미지 매칭 도구                    |
| `apps/backend-api-prototype/`                  | 추천·이미지 처리 API prototype      |
| `apps/fastapi-web-prototype/`                  | 이미지 업로드와 추천 화면 prototype |

## Related Documents

| Area                          | Document                                                            |
| ----------------------------- | ------------------------------------------------------------------- |
| Recommendation architecture   | `docs/06-architecture/ai-recommendation-architecture.md`            |
| Color extraction pipeline     | `docs/06-architecture/color-extraction-pipeline.md`                 |
| Emotion mapping pipeline      | `docs/06-architecture/emotion-mapping-pipeline.md`                  |
| Similarity ranking            | `docs/06-architecture/similarity-ranking-logic.md`                  |
| Color analysis summary        | `docs/14-ai-experiments/color-analysis-summary.md`                  |
| Emotion and color table       | `docs/14-ai-experiments/emotion-and-color-table-summary.md`         |
| Multimodal emotion extraction | `docs/14-ai-experiments/multimodal-emotion-extraction.md`           |
| Recommendation algorithm      | `docs/14-ai-experiments/recommendation-algorithm-summary.md`        |
| Space artwork recommendation  | `docs/18-space-recommendation/space-artwork-recommendation-flow.md` |

## Management Policy

`experiments/`에는 실험 재현과 기능 검토에 필요한 최소 자료만 포함한다.

다음 항목은 포함하지 않는다.

- 개인 정보가 포함된 자료
- 원본 사업 문서 전체 파일
- 대용량 이미지 결과물
- 임시 실행 결과물
- 자동 생성 cache
- 가상환경 폴더
- IDE 설정 폴더
- 비공개 설정값
- 외부 공개가 어려운 인증 정보

## Suggested Review Order

RestArt의 실험 구조를 확인할 때는 다음 순서로 보는 것이 좋다.

1. `experiments/color-clustering-prototypes/README.md`
2. `docs/14-ai-experiments/color-analysis-summary.md`
3. `docs/06-architecture/color-extraction-pipeline.md`
4. `experiments/multimodal-emotion-extraction/README.md`
5. `docs/14-ai-experiments/multimodal-emotion-extraction.md`
6. `docs/06-architecture/emotion-mapping-pipeline.md`
7. `docs/14-ai-experiments/recommendation-algorithm-summary.md`

## Notes

이 폴더의 자료는 실험 검토 단계의 산출물이다. 실제 서비스 적용 시에는 다음 사항을 추가로 정리해야 한다.

- 입력 데이터 형식
- 출력 데이터 형식
- 사용 library version
- 실행 환경
- 결과 검증 기준
- backend API와의 연결 방식
- 추천 ranking에 반영되는 기준

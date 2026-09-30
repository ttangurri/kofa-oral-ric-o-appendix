# 한국영상자료원 구술 아카이브 RiC-O 사례 데이터 (석사학위논문 부록 2·3)

[English](README.en.md) | **한국어**

석사학위논문 「한국영상자료원 원로영화인 구술 아카이브의 관계 기반 탐색을 위한 기술요소 설계 — RiC-O 적용을 중심으로」(충남대학교 대학원 기록학과, 오유리)의 **부록 2(RiC-O 인스턴스 데이터)** 와 **부록 3(적합 질의와 실행 결과)** 을 재사용 가능한 형태로 수록한 저장소입니다.

| 폴더 | 내용 | 안내 |
|---|---|---|
| [`appendix2/`](appendix2/) | RiC-O v1.1 기반 인스턴스 데이터 (Turtle, 280트리플) | [README](appendix2/README.md) · [English](appendix2/README.en.md) |
| [`appendix3/`](appendix3/) | SPARQL 적합 질의 Q1~Q7, 보조 질의, 실행 결과, 재실행 스크립트 | [README](appendix3/README.md) · [English](appendix3/README.en.md) |

## 빠른 재현

```bash
pip install rdflib
python appendix3/run_queries.py
```

280트리플이 로드되고, 질의별 반환 행 수(Q1 3 · Q2 2 · Q3 9 · Q4 2 · Q5 1 · Q6 1 · Q7 7 · 보조 3)가 출력됩니다.

## 유의 사항

- 본 데이터는 논문 4.4절의 **한정된 사례 데이터**(합작영화 군집 및 보조표본)이며, 한국영상자료원 구술 아카이브 전체를 나타내지 않습니다.
- 네임스페이스 `http://kofa.example.org/oral/` 는 **예시용(placeholder) 네임스페이스**로, 한국영상자료원이 발행한 식별자가 아닙니다.
- 데이터는 공개 메타데이터와 구술채록문·자료집을 근거로 하며, 각 관계의 근거 층위는 Turtle 파일의 주석과 `rico:relationSource`에 표시되어 있습니다.
- 논문 본문이 최종본이며, 본 저장소와 차이가 있을 경우 논문을 따릅니다.

## 라이선스

[CC BY 4.0](LICENSE) — 출처(오유리, 충남대학교 대학원 석사학위논문 부록)를 표시하면 자유롭게 이용·수정·재배포할 수 있습니다.

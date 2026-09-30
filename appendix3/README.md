# Appendix 3. Conformance Queries and Execution Results

Conformance queries Q1–Q7 were run against the explicit instance triples of [Appendix 2](../appendix2/README.md). They use SPARQL 1.1, and results are returned over the **graph before inference**.

## Execution environment

| Item | Detail |
|---|---|
| Vocabulary | RiC-O 1.1 (2025-05-22) |
| Data | 280 triples / 14 RiC-O classes / 18 properties |
| Query execution | Python 3.12 / RDFLib 7.6.0 / SPARQL 1.1 |
| Rows returned | Q1 3 · Q2 2 · Q3 9 · Q4 2 · Q5 1 · Q6 1 · Q7 7 |

In the thesis, syntax parsing and vocabulary checks were performed and the results of all seven queries were confirmed. The OWL RL rule-inference check merged RiC-O with the case data to look for explicit class-disjointness conflicts; it is **distinct from full OWL DL consistency checking**.

## Layout

- [`queries/`](queries/) — query files (`.rq`)
- [`results/`](results/) — results (CSV, UTF-8 with BOM)
- [`run_queries.py`](run_queries.py) — re-run script

```bash
pip install rdflib
python appendix3/run_queries.py
```

## Queries and results

Query text and result values are in Korean, as in the thesis.

### Q1. Co-production participants and their life-history records

- Query: [`queries/q1_coproduction_participants.rq`](queries/q1_coproduction_participants.rq)
- Rows returned: 3

| 구술자명 | 생애사구술 |
|---|---|
| 강범구(1924~, 감독) | 강범구 생애사 구술(2011) |
| 박행철(1934~, 제작자) | 박행철 생애사 구술(2014) |
| 정창화(1928~, 감독) | 정창화 생애사 구술(2008) |

### Q2. Life-history and thematic records of one person

- Query: [`queries/q2_same_person_records.rq`](queries/q2_same_person_records.rq)
- Rows returned: 2

| 기록 | 편성 |
|---|---|
| 강범구 생애사 구술(2011) | 생애사 구술 기록군 |
| 강범구 합작영화 주제사 구술(2014) | 합작영화 주제사 구술군(2014~2015, 17건) |

### Q3. Exploring records through the occupation hierarchy

- Query: [`queries/q3_occupation_hierarchy.rq`](queries/q3_occupation_hierarchy.rq)
- Rows returned: 9

| 직능 | 구술자명 | 기록 |
|---|---|---|
| 감독 | 강범구(1924~, 감독) | 강범구 생애사 구술(2011) |
| 감독 | 강범구(1924~, 감독) | 강범구 합작영화 주제사 구술(2014) |
| 감독 | 정창화(1928~, 감독) | 정창화 생애사 구술(2008) |
| 극장 영사 | 최치환(극장 영사) | 최치환 수입외화 주제사 구술(2020) |
| 수입 통관 | 지헌술(수입 통관) | 지헌술 수입외화 주제사 구술(2020) |
| 스태프 | 박남기(1935~, 현상·색보정) | 박남기 생애사 구술(2020) |
| 제작자 | 박행철(1934~, 제작자) | 박행철 생애사 구술(2014) |
| 제작자 | 박행철(1934~, 제작자) | 박행철 합작영화 주제사 구술(2014) |
| 현상·색보정 | 박남기(1935~, 현상·색보정) | 박남기 생애사 구술(2020) |

### Q4. Linking testimonies via an overarching mandate and its allocation reasons

- Query: [`queries/q4_mandate_allocation.rq`](queries/q4_mandate_allocation.rq)
- Rows returned: 2

| 기록단위 | 증언대상 |
|---|---|
| 강범구 생애사 제4차 구술채록문 | 수출 실적에 따른 외화수입쿼터 배정 |
| 박행철 생애사 구술(2014) | 반공영화 제작 실적에 따른 외화수입쿼터 배정 |

### Q5. Participants and testimony records at the customs stage

- Query: [`queries/q5_customs_stage.rq`](queries/q5_customs_stage.rq)
- Rows returned: 1

| 단계 | 참여자 | 증언기록 |
|---|---|---|
| 외화 수입 통관 | 지헌술(수입 통관) | 지헌술 수입외화 주제사 구술(2020) |

### Q6. Linking an experienced event to a testimony session

- Query: [`queries/q6_event_experience.rq`](queries/q6_event_experience.rq)
- Rows returned: 1

| 사건 | 경험자 | 증언회차 | 상위구술 |
|---|---|---|---|
| 1980년 국보위의 공직자 숙청 | 박남기(1935~, 현상·색보정) | 박남기 생애사 제4차 구술채록문 | 박남기 생애사 구술(2020) |

### Q7. Expanding across records through a shared activity

- Query: [`queries/q7_shared_activity.rq`](queries/q7_shared_activity.rq)
- Rows returned: 7

| 도달기록 | 관계유형 |
|---|---|
| 강범구 생애사 구술(2011) | 일반 주제(주 주제 여부 미지정) |
| 강범구 생애사 제3차 구술채록문 | 일반 주제(주 주제 여부 미지정) |
| 강범구 생애사 제4차 구술채록문 | 일반 주제(주 주제 여부 미지정) |
| 박행철 생애사 구술(2014) | 일반 주제(주 주제 여부 미지정) |
| 강범구 합작영화 주제사 구술(2014) | 주 주제 |
| 박행철 합작영화 주제사 구술(2014) | 주 주제 |
| 합작영화 주제사 구술군(2014~2015, 17건) | 주 주제 |

### 보조. Provenance of each relation

- Query: [`queries/aux_relation_source.rq`](queries/aux_relation_source.rq)
- Rows returned: 3

| 관계 | 출처 |
|---|---|
| http://kofa.example.org/oral/rel_CoProd_Quota_byEditor | 근거: 강범구 생애사 자료집 267쪽 각주 / 부속 기술 층위. |
| http://kofa.example.org/oral/rel_CoProd_Quota_bySpeaker | 근거: 강범구 생애사 제4차 구술채록문 261쪽·270–271쪽 / 채록문 본문 층위. |
| http://kofa.example.org/oral/rel_GoInHa_identity | 근거: 고인하 주제사 회차별 상세목록의 성명·작품 관여 정보 / 공개 메타데이터 층위 / 동일성 미확정. |

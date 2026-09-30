# 부록 2. RiC-O 인스턴스 데이터

[English](README.en.md) | **한국어**

논문 4.4절 사례 분석에 사용한 인스턴스 데이터 전체입니다.

- 파일: [`kofa_oral_instances.ttl`](kofa_oral_instances.ttl) (Turtle, UTF-8)
- 기준 어휘: RiC-O v1.1 (2025) — `https://www.ica.org/standards/RiC/ontology#`
- 규모: 온톨로지 헤더 포함 **280트리플**, RiC-O 클래스 **14종**, 프로퍼티 **18종**
- 네임스페이스: `kofa:` = `http://kofa.example.org/oral/` (예시용)

## 구성

| 절 | 내용 |
|---|---|
| 1 | 인물 개체(구술자·채록연구자, 구술 내용에 등장하는 인물) |
| 2 | 역할·직능·활동·법령 개체 (직능은 `hasOrHadPart`로 상·하위 연결) |
| 3 | 기록·기록군·표현형 개체 (Record, RecordPart, RecordSet, Instantiation) |
| 4 | 생산 관계의 실체화 (`CreationRelation`, 구술자와 채록연구자 역할 구별) |
| 5 | 증언 맥락의 삼각 구조 — 참여 관계 |
| 6 | 미확정 동일성의 기록 (고인하, `relationCertainty "uncertain"`) |
| 7 | 보조표본: 사건 개체(1980년 국보위 숙청)와 활동 층위 분화 |
| 8 | 규제 관계의 실체화 — 출처별 성격 진술의 분리 (`RuleRelation`) |
| 9 | 보조표본: 수입외화 주제사 구술 기록 |
| 10 | 관계별 출처 속성 (`rico:relationSource`, 3건) |

## 사용한 RiC-O 클래스(14)

Person, CorporateBody, Event, Activity, Mandate, OccupationType, RoleType, Record, RecordPart, RecordSet, Instantiation, CreationRelation, RuleRelation, Relation (+ `owl:NamedIndividual`, `owl:Ontology`)

## 읽는 법

- 근거 위치와 층위(`[공개 메타데이터 층위]`, `[채록문 본문 층위]`, `[부속 기술 층위]`)는 각 개체 아래 `#` 주석에 기재되어 있습니다.
- 관계의 방향은 Source=기록, Target=관여 행위자입니다. `RuleRelation`은 Source=법령, Target=활동입니다.

## 불러오기

```python
from rdflib import Graph
g = Graph().parse("kofa_oral_instances.ttl", format="turtle")
print(len(g))  # 280
```

Protégé, Apache Jena 등 Turtle을 지원하는 도구에서도 열 수 있습니다. 질의 예시는 [`../appendix3/`](../appendix3/README.md)를 참조하십시오.

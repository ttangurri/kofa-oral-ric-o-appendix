# Appendix 2. RiC-O Instance Data

The complete instance data used in the case analysis of thesis section 4.4.

- File: [`kofa_oral_instances.ttl`](kofa_oral_instances.ttl) (Turtle, UTF-8)
- Vocabulary: RiC-O v1.1 (2025) — `https://www.ica.org/standards/RiC/ontology#`
- Size: **280 triples** including the ontology header, **14 RiC-O classes**, **18 properties**
- Namespace: `kofa:` = `http://kofa.example.org/oral/` (placeholder)

## Structure

| Section | Contents |
|---|---|
| 1 | Person individuals (narrators, interviewers, persons mentioned in testimony) |
| 2 | Roles, occupations, activities, mandates (occupations linked via `hasOrHadPart`) |
| 3 | Records, record parts, record sets, instantiations |
| 4 | Reified creation relations (`CreationRelation`; narrator vs. interviewer roles) |
| 5 | Triangular structure of testimony context — participation relations |
| 6 | Unresolved identity (Go In-ha, `relationCertainty "uncertain"`) |
| 7 | Supplementary sample: an event (1980 purge) and activity-level differentiation |
| 8 | Reified regulation relations — separate statements by source (`RuleRelation`) |
| 9 | Supplementary sample: imported-film thematic oral records |
| 10 | Per-relation provenance (`rico:relationSource`, 3 statements) |

## RiC-O classes used (14)

Person, CorporateBody, Event, Activity, Mandate, OccupationType, RoleType, Record, RecordPart, RecordSet, Instantiation, CreationRelation, RuleRelation, Relation (plus `owl:NamedIndividual`, `owl:Ontology`)

## Reading the data

- Evidence locations and levels (`[public metadata level]`, `[transcript body level]`, `[accompanying description level]`; written in Korean in the source comments) are given in `#` comments under each individual.
- Relation direction: Source = record, Target = involved agent. For `RuleRelation`: Source = mandate, Target = activity.

## Loading

```python
from rdflib import Graph
g = Graph().parse("kofa_oral_instances.ttl", format="turtle")
print(len(g))  # 280
```

Any Turtle-capable tool (Protégé, Apache Jena, etc.) can open it. For example queries, see [`../appendix3/`](../appendix3/README.md).

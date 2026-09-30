# RiC-O Case Data for the Korean Film Archive's Oral History Collection (Thesis Appendices 2 & 3)

**English** | [한국어](README.md)

This repository holds, in reusable form, **Appendix 2 (RiC-O instance data)** and **Appendix 3 (conformance queries and execution results)** of the master's thesis *Designing Descriptive Elements for Relationship-Based Exploration of the Korean Film Archive's Oral History Collection: An Application of RiC-O* (Oh Yuri, Department of Archives Management, Graduate School, Chungnam National University).

| Folder | Contents | Guide |
|---|---|---|
| [`appendix2/`](appendix2/) | RiC-O v1.1 instance data (Turtle, 280 triples) | [README](appendix2/README.en.md) · [한국어](appendix2/README.md) |
| [`appendix3/`](appendix3/) | SPARQL conformance queries Q1–Q7, an auxiliary query, results, and a re-run script | [README](appendix3/README.en.md) · [한국어](appendix3/README.md) |

## Quick reproduction

```bash
pip install rdflib
python appendix3/run_queries.py
```

The script loads 280 triples and prints the row count of each query (Q1 3 · Q2 2 · Q3 9 · Q4 2 · Q5 1 · Q6 1 · Q7 7 · auxiliary 3).

## Notes

- The data is the **limited case dataset** of thesis section 4.4 (the co-production cluster plus supplementary samples). It does not represent the whole oral history collection.
- The namespace `http://kofa.example.org/oral/` is a **placeholder**; it is not an identifier issued by the Korean Film Archive.
- The data is grounded in public metadata and oral history transcripts/volumes. The evidence level of each relation is marked in the Turtle comments and in `rico:relationSource`.
- Labels and literals are in Korean. The thesis is the authoritative version; where this repository differs, the thesis prevails.

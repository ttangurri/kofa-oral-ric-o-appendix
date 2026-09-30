"""부록 3 질의 실행 스크립트 / Runs the Appendix 3 SPARQL queries against the Appendix 2 data.

Usage:  pip install rdflib && python appendix3/run_queries.py
Writes CSV results to appendix3/results/ and prints row counts.
"""
import csv
from pathlib import Path
from rdflib import Graph

ROOT = Path(__file__).resolve().parent.parent
g = Graph().parse(ROOT / "appendix2" / "kofa_oral_instances.ttl", format="turtle")
print(f"triples: {len(g)}")

out = ROOT / "appendix3" / "results"
out.mkdir(exist_ok=True)
for q in sorted((ROOT / "appendix3" / "queries").glob("*.rq")):
    res = g.query(q.read_text(encoding="utf-8"))
    rows = [[str(v) if v is not None else "" for v in r] for r in res]
    with open(out / (q.stem + ".csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow([str(v) for v in res.vars])
        w.writerows(rows)
    print(f"{q.stem}: {len(rows)} rows")

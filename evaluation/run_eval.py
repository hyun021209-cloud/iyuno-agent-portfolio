import json, time
from pathlib import Path
from app.rag import Retriever, answer

ROOT = Path(__file__).resolve().parents[1]
qs = json.loads((ROOT/"evaluation/questions.json").read_text(encoding="utf-8"))
r = Retriever(top_k=4)
rows=[]
for item in qs:
    out=answer(item["question"], r)
    rows.append({"question": item["question"], "latency_ms": out["latency_ms"],
                 "top_score": out["sources"][0]["score"] if out["sources"] else 0})
metrics={
    "num_questions": len(rows),
    "mean_latency_ms": sum(x["latency_ms"] for x in rows)/len(rows),
    "mean_top_score": sum(x["top_score"] for x in rows)/len(rows),
    "note": "2주차 베이스 평가. 4주차에 Recall@k/faithfulness를 정식 평가셋으로 확장."
}
(ROOT/"evaluation/metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(metrics, ensure_ascii=False, indent=2))

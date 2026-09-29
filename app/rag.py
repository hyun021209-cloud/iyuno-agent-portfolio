import json, re, time
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "data" / "documents.json"

def chunk_text(text, size=900, overlap=120):
    text = re.sub(r"\s+", " ", text).strip()
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + size)
        chunks.append(text[start:end])
        if end == len(text): break
        start = end - overlap
    return chunks

class Retriever:
    def __init__(self, top_k=4):
        self.top_k = top_k
        raw = json.loads(DOCS.read_text(encoding="utf-8"))
        self.items = []
        for d in raw:
            for j, c in enumerate(chunk_text(d["text"])):
                self.items.append({
                    "doc_id": d["id"], "chunk_id": j, "title": d["title"],
                    "org": d["org"], "url": d["url"], "text": c
                })
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=25000)
        self.matrix = self.vectorizer.fit_transform([x["text"] for x in self.items])

    def search(self, query):
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix).ravel()
        idx = scores.argsort()[::-1][:self.top_k]
        results = []
        for i in idx:
            item = dict(self.items[i])
            item["score"] = float(scores[i])
            results.append(item)
        return results

def answer(query, retriever=None):
    retriever = retriever or Retriever()
    t0 = time.perf_counter()
    results = retriever.search(query)
    latency_ms = (time.perf_counter() - t0) * 1000
    lines = [f"질문: {query}", "", "검색 근거:"]
    for n, r in enumerate(results, 1):
        excerpt = r["text"][:500].strip()
        lines.append(f"[{n}] {r['title']} ({r['org']})")
        lines.append(excerpt)
        lines.append(f"출처: {r['url']}")
    return {"answer": "\n".join(lines), "sources": results, "latency_ms": latency_ms}

if __name__ == "__main__":
    r = Retriever()
    q = input("질문: ")
    out = answer(q, r)
    print(out["answer"])
    print(f"\nlatency: {out['latency_ms']:.2f} ms")

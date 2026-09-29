import json, re, time
from pathlib import Path
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "documents.json"
SOURCES = ROOT / "data" / "sources.json"

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script","style","nav","footer","header"]):
        tag.decompose()
    text = soup.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", text)

def main():
    sources = json.loads(SOURCES.read_text(encoding="utf-8"))
    docs = []
    for i, src in enumerate(sources, 1):
        try:
            r = requests.get(src["url"], timeout=20, headers={"User-Agent":"student-rag-portfolio/1.0"})
            r.raise_for_status()
            text = clean_html(r.text)
            if len(text) < 300:
                raise ValueError("too little text")
            docs.append({**src, "id": f"doc-{i:02d}", "text": text})
            print(f"[OK] {i:02d} {src['title']} ({len(text)} chars)")
        except Exception as e:
            print(f"[WARN] {i:02d} {src['title']}: {e}")
    OUT.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"saved {len(docs)} documents -> {OUT}")

if __name__ == "__main__":
    main()

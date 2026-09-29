# AI Agent Portfolio — RAG + Tool Calling

채용공고의 AI/LLM 관련 요구사항을 실제 GitHub 결과물로 연결하기 위한 포트폴리오 프로젝트입니다.

## 1. 프로젝트 개요

공개된 OWASP 및 NIST 문서를 수집하고, 문서를 검색 가능한 형태로 구성하여 질문에 관련된 근거 문서를 검색하는 RAG(Retrieval-Augmented Generation) 기반 검색 시스템을 구현했습니다.

주요 구성:

- 20개 공개 문서 수집 및 전처리
- 문서 Chunking
- TF-IDF 기반 Retriever
- Cosine Similarity 기반 검색
- 검색 결과의 출처 URL 제공
- Python Tool 구현
- pytest 자동 테스트
- GitHub Actions CI

## 2. 프로젝트 구조

```text
iyuno-agent-portfolio/
├── app/
│   ├── ingest.py
│   ├── rag.py
│   ├── agent.py
│   ├── tools.py
│   └── streamlit_app.py
├── data/
│   ├── sources.json
│   └── documents.json
├── evaluation/
│   ├── questions.json
│   └── run_eval.py
├── tests/
│   └── test_tools.py
├── .github/
│   └── workflows/
├── README.md
├── REFLECTION.md
└── requirements.txt

## 3. 실행 방법
설치
python -m pip install -r requirements.txt
문서 수집
python -m app.ingest

20개 공개 문서를 정상적으로 수집했습니다.

RAG 검색 실행
python -m app.rag

질문을 입력하면 관련 문서를 검색하고 문서 제목, 기관, 내용 일부와 출처 URL을 제공합니다.

테스트 실행
python -m pytest -q

실행 결과:

5 passed

## 4. 실험 결과
항목	결과
수집 문서	20개
RAG 검색	정상 실행
검색 결과	Top 4
출처 표시	URL 제공
측정 latency	약 2.30 ms
pytest	5 passed
GitHub Actions	성공

※ latency는 로컬 환경에서 단일 검색을 실행했을 때 측정된 값이며, 시스템 환경에 따라 달라질 수 있습니다.

## 5. 구현 특징
Retriever

TF-IDF Vectorizer를 이용해 문서 Chunk를 벡터화하고 Cosine Similarity를 이용해 질문과 관련성이 높은 문서를 검색합니다.

Citation

검색 결과마다 원문 문서의 출처 URL을 함께 표시하여 검색 근거를 확인할 수 있도록 구성했습니다.

Testing

pytest를 이용하여 Tool 기능에 대한 5개의 테스트를 작성하고 GitHub Actions에서 자동으로 테스트하도록 구성했습니다.

## 6. 한계

현재 구현은 기본적인 검색 기반 RAG 구조에 초점을 맞추고 있습니다.

TF-IDF 기반 검색이므로 의미 기반 임베딩 검색과 차이가 있을 수 있습니다.
현재 검색 결과를 바탕으로 한 최종 자연어 생성 기능은 제한적입니다.
평가 데이터셋의 규모가 크지 않아 검색 성능을 일반화하기에는 한계가 있습니다.
latency는 로컬 실행 환경의 측정값입니다.

## 7. 재현 명령어
python -m pip install -r requirements.txt
python -m app.ingest
python -m app.rag
python -m pytest -q

## 8. GitHub Actions

GitHub Actions를 이용하여 저장소에 변경사항이 발생하면 Python 환경을 구성하고 의존성을 설치한 뒤 pytest를 자동 실행하도록 구성했습니다.

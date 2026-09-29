# iyuno-agent-portfolio

채용공고의 요구사항을 작동하는 GitHub 프로젝트로 증명하기 위한 포트폴리오입니다.

## 프로젝트
**Agentic Knowledge Triage** — 공개 보안·기술 문서를 검색하고 질문에 근거와 함께 답하는 간단한 RAG 시스템.

### 채용공고 요구사항 ↔ 구현
| 공고 요구사항 | 프로젝트 증거 |
|---|---|
| LLM 기반 AI Agent 시스템 설계·개발 | `app/agent.py` |
| RAG 검색·응답 시스템 | `app/rag.py` |
| Tool calling / API | `app/tools.py` |
| 다단계 workflow | `app/agent.py`의 route → retrieve → answer 흐름 |
| 평가·피드백 루프 | `evaluation/questions.json`, `evaluation/run_eval.py` |
| latency / reliability 개선 | evaluation 결과와 테스트로 측정 |

## 2주차 목표
첨부된 수업 자료의 2주차 목표인 **공개 문서 20개 ingest + RAG 구현**을 중심으로 작성했습니다.

## 설치

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

## 문서 수집
```bash
python -m app.ingest
```

기본적으로 `data/sources.json`에 기록된 공개 문서 URL을 읽어 텍스트를 수집합니다.

> 인터넷 접근이 필요한 단계입니다. 문서의 이용조건/robots 정책을 확인하고 공개적으로 허용된 자료만 사용하세요.

## RAG 실행
```bash
python -m app.rag
```

## Streamlit 데모
```bash
streamlit run app/streamlit_app.py
```

## 테스트
```bash
pytest -q
```

## 평가
```bash
python evaluation/run_eval.py
```

평가 결과는 `evaluation/metrics.json`에 저장됩니다.

## 현재 단계의 한계
- 실제 LLM API를 연결하지 않은 2주차 베이스입니다.
- 기본 검색은 재현성을 위해 TF-IDF를 사용하며, `sentence-transformers`를 설치하면 임베딩 검색으로 확장할 수 있습니다.
- 3주차에는 실제 tool calling과 API orchestration을 추가합니다.
- 4주차에는 30개 이상 질문과 Recall@k / faithfulness / latency 측정을 확장합니다.

## 데이터 출처
`data/sources.json`에 URL, 문서명, 기관, 수집일을 기록합니다.

## 과제 출처
수업 제공 자료: **REAL JOB POSTING → REAL GITHUB PROJECT / Korea Job Posting → GitHub Evidence**.

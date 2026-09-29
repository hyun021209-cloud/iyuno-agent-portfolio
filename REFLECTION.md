# 최종 1페이지 회고 — 2주차

## 무엇을 구현했는가?
공개 보안·기술 문서를 대상으로 문서를 수집하고, 일정 길이로 chunking한 뒤 TF-IDF 기반 vector search로 질문과 관련된 문서를 검색하는 RAG 베이스를 구현했다. 검색 결과에는 문서명과 원문 URL을 함께 표시하여 답변의 근거를 확인할 수 있도록 했다.

## 채용공고와 어떻게 연결되는가?
Iyuno AI Agent Engineer 공고에서 제시한 RAG 검색·응답 시스템 요구사항을 프로젝트의 핵심 기능으로 대응시켰다. Agent workflow의 형태를 만들고, 이후 tool calling, API orchestration, evaluation으로 확장할 수 있도록 구조를 분리했다.

## AI를 어떻게 활용했는가?
프로젝트 구조, 함수 설계, 테스트 아이디어, 오류 수정 과정에서 생성형 AI를 보조 도구로 사용한다. 생성된 코드는 실행 결과를 확인하고 필요한 부분을 직접 수정·검증한다.

## 남은 과제
3주차: 실제 tool calling 및 API 연동.
4주차: 30개 이상 평가 질문, Recall@k/faithfulness/latency 측정.
5주차: FastAPI 또는 Streamlit 배포와 2분 이내 데모 영상.

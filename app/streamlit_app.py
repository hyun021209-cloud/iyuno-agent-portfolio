import streamlit as st
from app.rag import Retriever, answer

st.set_page_config(page_title="Agentic Knowledge Triage", page_icon="🔎")
st.title("🔎 Agentic Knowledge Triage")
st.caption("공개 보안·기술 문서 기반 RAG 데모 — 2주차 베이스")

@st.cache_resource
def load():
    return Retriever(top_k=4)

q = st.text_input("질문을 입력하세요", "What is the NIST Cybersecurity Framework?")
if q:
    with st.spinner("문서를 검색하는 중..."):
        result = answer(q, load())
    st.markdown(result["answer"])
    st.metric("검색 latency", f"{result['latency_ms']:.1f} ms")

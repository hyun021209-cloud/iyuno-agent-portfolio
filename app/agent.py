from .rag import Retriever, answer

class KnowledgeAgent:
    """2주차용 최소 Agent workflow: route -> retrieve -> evidence response."""
    def __init__(self):
        self.retriever = Retriever()

    def run(self, question):
        # 향후 3주차에서 tool calling/API orchestration을 이 단계에 연결합니다.
        return answer(question, self.retriever)

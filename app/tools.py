def calculator(expression: str):
    """데모용 계산기 tool. 3주차에서 실제 tool calling에 연결."""
    allowed = set("0123456789+-*/(). %")
    if not set(expression) <= allowed:
        raise ValueError("허용되지 않은 수식입니다.")
    return eval(expression, {"__builtins__": {}}, {})

def source_policy():
    """향후 정책 조회 API를 연결할 자리."""
    return {"status": "demo", "message": "3주차에서 외부 API로 교체"}

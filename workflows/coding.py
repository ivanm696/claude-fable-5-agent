"""Agentic coding workflow: plan → implement → test → self-review."""
from agent.core import ClaudeFable5Agent


def run_coding_agent(task: str) -> dict:
    """Run a multi-stage coding workflow with self-verification."""
    agent = ClaudeFable5Agent()

    plan = agent.chat(f"""
    Задача: {task}

    Сначала составь детальный план реализации.
    Разбей на этапы и определи возможные сложности.
    """)

    code = agent.chat("""
    Теперь реализуй план. Напиши полный рабочий код.
    Включи комментарии и обработку ошибок.
    """)

    tests = agent.chat("""
    Напиши тесты для проверки кода.
    Покрой основные сценарии и граничные случаи.
    """)

    review = agent.chat("""
    Проверь свою работу:
    1. Соответствует ли код исходной задаче?
    2. Есть ли баги или улучшения?
    3. Финальная оценка качества.
    """)

    return {"plan": plan, "code": code, "tests": tests, "review": review}

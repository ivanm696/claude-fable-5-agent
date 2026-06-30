"""Deep research workflow: gather, synthesize, cross-check."""
from agent.core import ClaudeFable5Agent


def run_research_agent(topic: str) -> dict:
    agent = ClaudeFable5Agent()

    outline = agent.chat(f"Составь план исследования по теме: {topic}")
    findings = agent.chat("Проведи анализ по каждому пункту плана детально.")
    summary = agent.chat("Сделай итоговое резюме с ключевыми выводами.")

    return {"outline": outline, "findings": findings, "summary": summary}

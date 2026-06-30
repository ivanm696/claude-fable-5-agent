"""Enterprise workflow: document analysis, reporting, multi-step business tasks."""
from agent.core import ClaudeFable5Agent
from agent.vision import analyze_image


def run_document_workflow(document_text: str, task: str) -> dict:
    agent = ClaudeFable5Agent()

    analysis = agent.chat(f"""
    Документ:
    {document_text}

    Задача: {task}

    Проанализируй документ и выполни задачу.
    """)

    report = agent.chat("Составь краткий итоговый отчёт по результатам анализа.")

    return {"analysis": analysis, "report": report}


def run_visual_document_workflow(image_path: str, task: str) -> dict:
    """For scanned documents, charts, or diagrams."""
    description = analyze_image(image_path, f"Проанализируй изображение. Задача: {task}")
    return {"description": description}

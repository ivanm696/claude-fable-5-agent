"""Example: analyzing a scanned document or chart."""
from workflows.enterprise import run_visual_document_workflow

if __name__ == "__main__":
    result = run_visual_document_workflow(
        "path/to/document.png",
        "Извлеки ключевые цифры и тренды из этого графика."
    )
    print(result["description"])

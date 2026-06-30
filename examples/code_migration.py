"""Example: large codebase migration task."""
from workflows.coding import run_coding_agent

if __name__ == "__main__":
    result = run_coding_agent(
        "Перенести проект с Python 2 на Python 3: обнови синтаксис print, "
        "обработку исключений и работу со строками/байтами."
    )
    for stage, content in result.items():
        print(f"\n=== {stage.upper()} ===\n{content}\n")

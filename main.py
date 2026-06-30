from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from agent.core import ClaudeFable5Agent

console = Console()


def main() -> None:
    console.print(Panel.fit(
        "[bold cyan]🤖 Claude Fable 5 Agent[/bold cyan]\n"
        "[dim]Введите 'выход' для завершения | 'сброс' для новой сессии[/dim]",
        border_style="cyan",
    ))

    try:
        agent = ClaudeFable5Agent()
    except RuntimeError as e:
        console.print(f"[bold red]{e}[/bold red]")
        return

    while True:
        user_input = Prompt.ask("\n[bold green]Вы[/bold green]")

        if user_input.lower() in ("выход", "exit", "quit"):
            console.print("[bold red]До свидания![/bold red]")
            break
        if user_input.lower() in ("сброс", "reset"):
            agent.reset()
            continue
        if not user_input.strip():
            continue

        console.print("\n[bold blue]Агент думает...[/bold blue]")
        try:
            response = agent.chat(user_input)
        except Exception as e:
            console.print(f"[bold red]Ошибка: {e}[/bold red]")
            continue
        console.print(Panel(response, title="[bold blue]🤖 Fable 5[/bold blue]", border_style="blue"))


if __name__ == "__main__":
    main()

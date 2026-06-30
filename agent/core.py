"""
Claude Fable 5 Agent — core conversational agent.

Fable 5 is a Mythos-class model: adaptive thinking is always on and
cannot be disabled via the API. Do NOT pass thinking={"type": "disabled"}
— it returns a 400 error. Simply omit the thinking parameter.

Some queries in cybersecurity/biology/chemistry/nuclear domains are
automatically rerouted by Anthropic's safety classifiers to Opus 4.8.
When that happens the response includes stop_reason == "refusal" with
a stop_details object — handle it explicitly rather than treating it
as a normal completion.
"""
import os
from anthropic import Anthropic
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()

MODEL = "claude-fable-5"
MAX_TOKENS = 8096


class ClaudeFable5Agent:
    def __init__(self, model: str = MODEL, max_tokens: int = MAX_TOKENS):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key."
            )
        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.conversation_history: list[dict] = []
        self.system_prompt = (
            "Ты — мощный ИИ-агент Claude Fable 5.\n"
            "Ты способен:\n"
            "- Решать многодневные сложные задачи\n"
            "- Писать, тестировать и проверять код\n"
            "- Анализировать документы, PDF, диаграммы и изображения\n"
            "- Делегировать подзадачи и проверять собственную работу\n"
            "- Выполнять корпоративные рабочие процессы\n"
            "Всегда проверяй свою работу перед тем, как представить результат."
        )

    def chat(self, user_message: str) -> str:
        self.conversation_history.append({"role": "user", "content": user_message})

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=self.conversation_history,
            # NOTE: do not pass `thinking` here — Fable 5 keeps adaptive
            # thinking on permanently and rejects an explicit disable.
        )

        # Fable 5's safety classifiers can reroute risky requests; surface
        # that distinctly instead of silently returning Opus 4.8's reply.
        if getattr(response, "stop_reason", None) == "refusal":
            details = getattr(response, "stop_details", None)
            category = getattr(details, "category", "unknown") if details else "unknown"
            note = f"[Запрос перенаправлен фильтрами безопасности ({category})]"
            console.print(f"[yellow]{note}[/yellow]")

        text_blocks = [block.text for block in response.content if block.type == "text"]
        assistant_message = "\n".join(text_blocks) if text_blocks else ""

        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        return assistant_message

    def reset(self) -> None:
        self.conversation_history = []
        console.print("[yellow]История разговора сброшена.[/yellow]")

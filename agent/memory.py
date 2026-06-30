"""Long-term context: persist conversation history to disk between sessions."""
import json
from pathlib import Path


class ConversationMemory:
    def __init__(self, path: str = ".agent_memory.json") -> None:
        self.path = Path(path)

    def save(self, history: list[dict]) -> None:
        self.path.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")

    def load(self) -> list[dict]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def clear(self) -> None:
        if self.path.exists():
            self.path.unlink()

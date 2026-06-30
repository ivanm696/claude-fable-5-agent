"""Tool-use helpers for Claude Fable 5. Same tool schema as Opus 4.8 / Sonnet 4.6."""
from typing import Any, Callable


class ToolRegistry:
    """Maps tool names to Python callables and builds the Claude `tools` schema."""

    def __init__(self) -> None:
        self._tools: dict[str, dict[str, Any]] = {}
        self._handlers: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, description: str, input_schema: dict[str, Any]):
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self._tools[name] = {
                "name": name,
                "description": description,
                "input_schema": input_schema,
            }
            self._handlers[name] = func
            return func
        return decorator

    @property
    def schema(self) -> list[dict[str, Any]]:
        return list(self._tools.values())

    def call(self, name: str, **kwargs: Any) -> Any:
        if name not in self._handlers:
            raise KeyError(f"No tool registered with name '{name}'")
        return self._handlers[name](**kwargs)


tools = ToolRegistry()


@tools.register(
    "read_file",
    "Read the contents of a text file from disk.",
    {
        "type": "object",
        "properties": {"path": {"type": "string", "description": "File path to read"}},
        "required": ["path"],
    },
)
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@tools.register(
    "write_file",
    "Write text content to a file on disk.",
    {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "File path to write"},
            "content": {"type": "string", "description": "Content to write"},
        },
        "required": ["path", "content"],
    },
)
def write_file(path: str, content: str) -> str:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Written {len(content)} chars to {path}"

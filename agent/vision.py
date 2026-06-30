"""Vision helpers — analyze images, charts, and diagrams with Claude Fable 5."""
import base64
import os
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-fable-5"

_MEDIA_TYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}


def analyze_image(image_path: str, question: str = "Опиши это изображение подробно.") -> str:
    """Analyze an image, chart, diagram, or screenshot."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set.")

    client = Anthropic(api_key=api_key)

    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    image_data = path.read_bytes()
    base64_image = base64.standard_b64encode(image_data).decode("utf-8")

    ext = path.suffix.lower()
    media_type = _MEDIA_TYPES.get(ext)
    if media_type is None:
        raise ValueError(f"Unsupported image format: {ext}. Supported: {list(_MEDIA_TYPES)}")

    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": base64_image,
                        },
                    },
                    {"type": "text", "text": question},
                ],
            }
        ],
    )

    text_blocks = [block.text for block in response.content if block.type == "text"]
    return "\n".join(text_blocks)




from __future__ import annotations

BASE_URL = "https://api.airforce"
CHAT_PATH = "/v1/chat/completions"
MODELS_PATH = "/v1/models"

MODELS: list[str] = ["roleplay:free"]
CAPS: dict[str, bool] = {
    "chat": True,
    "completions": True,
    "responses": True,
    "tools": True,
    "native_tools": True,
}

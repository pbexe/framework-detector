import importlib.resources
from framework_detector import frameworks
from pathlib import Path
import json
from typing import Any


def detect(path: Path) -> str:
    for value in importlib.resources.contents(frameworks):
        if value.endswith(".json") and importlib.resources.is_resource(
            frameworks, value
        ):
            data = json.loads(importlib.resources.read_text(frameworks, value))
            if check_match(path, data):
                return data["name"]


def check_match(path: Path, data: dict[str, Any]) -> bool:
    for file in data["detect"]:
        if (path / file).exists():
            if data["detect"][file] is None:
                return True
            else:
                file_text = (path / file).read_text()
                for substring in data["detect"][file]:
                    if substring in file_text:
                        return True
    return False


if __name__ == "__main__":
    print(detect(Path.cwd()))

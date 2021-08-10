import importlib.resources
from . import frameworks


def main() -> None:
    print(importlib.resources.read_text(frameworks, 'test.json'))

import importlib.resources
from . import frameworks

def main():
    print(importlib.resources.read_text(frameworks, 'test.json'))
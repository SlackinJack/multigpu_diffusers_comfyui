from importlib import import_module
from pathlib import Path

__all__ = [
    path.stem
    for path in Path(__file__).parent.glob("*.py")
    if path.name != "__init__.py" and not path.stem.startswith("_")
]

for module_name in __all__:
    import_module(f".{module_name}", package=__name__)

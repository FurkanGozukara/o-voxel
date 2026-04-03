from importlib import import_module
import torch  # noqa: F401

_C = import_module("._C", __name__)

__all__ = ["_C", "convert", "io", "postprocess", "rasterize", "serialize"]


def __getattr__(name):
    if name in {"convert", "io", "postprocess", "rasterize", "serialize"}:
        module = import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

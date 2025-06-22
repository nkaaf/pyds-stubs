# ruff: noqa: N801

from typing import Generic, TypeVar

_T = TypeVar("_T")
_TL = TypeVar("_TL")

__all__ = ["GList", "capsule"]

class capsule(Generic[_T]):
    def __init__(self, data: _T) -> None: ...

class GList(Generic[_TL]):
    data: capsule[_TL]
    next: GList[_TL]
    prev: GList[_TL]

    def __init__(self, data: _TL) -> None: ...

# ruff: noqa: N801
# ruff: noqa: UP045 - This check is for Python >= 3.10

from typing import Generic, Optional, TypeVar

_T = TypeVar("_T")
_TL = TypeVar("_TL")

__all__ = ["GList", "capsule"]

class capsule(Generic[_T]):
    def __init__(self, data: _T) -> None: ...

class GList(Generic[_TL]):
    data: capsule[_TL]
    next: Optional[GList[_TL]]
    prev: Optional[GList[_TL]]

    def __init__(self, data: _TL) -> None: ...

# ruff: noqa: N801

from typing import TypeVar

_T = TypeVar('_T')
_TL = TypeVar('_TL')

__all__ = ['GList', 'capsule']

class capsule(_T):
    def __init__(self, data: _T) -> None: ...

class GList(_TL):
    data: capsule[_TL]
    next: GList[_TL] | None
    prev: GList[_TL] | None

    def __init__(self, data: _TL) -> None: ...

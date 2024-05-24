from __future__ import annotations

from typing import Any

from statisfactory.ir.operation import operation


class product(operation):
    def __init__(self, multiplicands: list[Any]):
        desc: dict[str, Any] = {}
        super().__init__(multiplicands, desc)

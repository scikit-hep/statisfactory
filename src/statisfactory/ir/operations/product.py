from __future__ import annotations

from ..operation import operation


class product(operation):
    def __init__(self, multiplicands: list):
        desc = {}
        super().__init__(multiplicands, desc)

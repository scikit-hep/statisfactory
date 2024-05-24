from __future__ import annotations

from typing import Any
from uuid import uuid4

from statisfactory.ir.ir_base import ir_base


class operation(ir_base):
    def __init__(self, operands: list[str], description: dict[str, Any]):
        self._operands = operands
        deps = {uuid4().hex: operand for operand in operands}
        super().__init__(deps, description)

    def __repr__(self) -> str:
        out = str(type(self)) + " :\t\n"
        out += "\toperands     : [\n"
        for op in self._operands:
            out += " " + str(op) + "\n"
        out += " ]"
        return out

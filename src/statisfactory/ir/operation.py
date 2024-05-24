from __future__ import annotations

from uuid import uuid4

from .ir_base import ir_base


class operation(ir_base):
    def __init__(self, operands: list, description: dict):
        self._operands = operands
        deps = {uuid4().hex: operand for operand in operands}
        super().__init__(deps, description)

    def __repr__(self):
        out = str(type(self)) + " :\t\n"
        out += "\toperands     : [\n"
        for op in self._operands:
            out += " " + str(op) + "\n"
        out += " ]"
        return out

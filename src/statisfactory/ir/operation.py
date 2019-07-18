from .ir_base import ir_base
import pprint as pp
from uuid import uuid4


class operation(ir_base):
    def __init__(self, operands: list, description: dict):
        self._operands = operands
        deps = {uuid4().hex: operand for operand in operands}
        super(operation, self).__init__(deps, description)

    def __repr__(self):
        out = str(type(self)) + ' :\t\n'
        out += '\toperands     : [\n'
        for op in self._operands:
            out += ' ' + str(op) + '\n'
        out += ' ]'
        return out

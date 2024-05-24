from __future__ import annotations

import pprint as pp

from .ir_base import ir_base


class distribution(ir_base):
    def __init__(self, observables: dict, parameters: dict, description: dict):
        self._observables = observables
        self._parameters = parameters
        deps = {}
        deps.update(observables)
        for k, p in parameters.items():
            if k in deps:
                msg = f"key {k} already in dependencies"
                raise ValueError(msg)

            deps[k] = p
        if "expression" not in description:
            msg = "Distributions must have an expression in their description"
            raise ValueError(msg)
        super().__init__(deps, description)

    def __repr__(self):
        out = str(type(self)) + " :\t\n"
        out += "\tobservables : " + pp.pformat(self._observables) + "\n"
        out += "\tparameters  : " + pp.pformat(self._parameters) + "\n"
        out += "\texpression  : " + pp.pformat(self._description["expression"])
        return out

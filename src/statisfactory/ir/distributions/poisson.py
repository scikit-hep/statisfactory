from __future__ import annotations

from ..distribution import distribution


class poisson(distribution):
    def __init__(self, x, mean):
        obs = {"x": x}
        params = {"mean": mean}
        desc = {"expression": "(mean**x)*exp(mean)/factorial(x)"}
        super().__init__(obs, params, desc)

from __future__ import annotations

from statisfactory.ir.distribution import distribution


class poisson(distribution):
    def __init__(self, x: str, mean: str):
        obs = {"x": x}
        params = {"mean": mean}
        desc = {"expression": "(mean**x)*exp(mean)/factorial(x)"}
        super().__init__(obs, params, desc)

from __future__ import annotations

from statisfactory.ir.distribution import distribution


class gaussian(distribution):
    def __init__(self, x: str, mean: str, sigma: str):
        obs = {"x": x}
        params = {"mean": mean, "sigma": sigma}
        desc = {"expression": "exp(-0.5*((x-mean)/sigma)**2"}
        super().__init__(obs, params, desc)

from __future__ import annotations

import pprint
from typing import Any


class ir_base:
    def __init__(self, dependencies: dict[str, Any], description: dict[str, Any]):
        self._dependencies = dependencies
        self._description = description

    @property
    def dependencies(self) -> dict[str, Any]:
        return self._dependencies

    @property
    def description(self) -> dict[str, Any]:
        return self._description

    def __repr__(self) -> str:
        out = str(type(self)) + ":\n"
        out += "\tdependencies: " + pprint.pformat(self._dependencies)
        out += "\n"
        out += "\tdescription : " + pprint.pformat(self._description)
        return out

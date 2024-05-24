from __future__ import annotations

import importlib.metadata

import statisfactory as m


def test_version():
    assert importlib.metadata.version("statisfactory") == m.__version__

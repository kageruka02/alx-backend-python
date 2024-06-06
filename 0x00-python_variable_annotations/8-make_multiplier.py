#!/usr/bin/env python3
"user annotations"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(v: float) -> float:
        return v * multiplier

    return multiplier_function

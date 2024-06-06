#!/usr/bin/env python3
"basic annotation"
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "returns tuple the first one as string and second float"
    return {k, v**2}

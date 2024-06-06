#!/usr/bin/env python3
"basics annotation"
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    "basics annotation"
    return [(i, len(i)) for i in lst]

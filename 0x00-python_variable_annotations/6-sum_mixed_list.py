#!/usr/bin/env python3
"basic annotations"
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "returning sum of a list of floats and integers"
    return sum(mxd_lst)

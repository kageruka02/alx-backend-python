#!/usr/bin/env python3
from typing import List

"basic annotations"


def sum_list(input_list: List[float]) -> float:
    "return sum of floats in list"
    return sum([num for num in input_list])

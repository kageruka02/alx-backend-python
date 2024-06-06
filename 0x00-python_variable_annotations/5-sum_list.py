#!/usr/bin/env python3
"basic annotations"


def sum_list(input_list: list[float]) -> float:
    "return sum of floats in list"
    return sum([num for num in input_list])

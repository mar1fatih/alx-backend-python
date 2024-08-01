#!/usr/bin/env python3
"""notated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list function"""
    c: float = 0
    for item in input_list:
        c += item
    return c

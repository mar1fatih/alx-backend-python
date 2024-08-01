#!/usr/bin/env python3
"""annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sum_mixed_list function"""
    c: Union[int, float] = 0
    for item in mxd_lst:
        c += item
    return c

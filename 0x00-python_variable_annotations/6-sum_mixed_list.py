#!/usr/bin/env python3
"""annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list function"""
    c: float = 0.0
    for item in mxd_lst:
        c += float(item)
    return c

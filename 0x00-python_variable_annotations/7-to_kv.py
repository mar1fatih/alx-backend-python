#!/usr/bin/env python3
"""annotated function 7-to_kv.py"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv func"""
    new_tuple: Tuple[str, float] = (k, v * v)
    return new_tuple

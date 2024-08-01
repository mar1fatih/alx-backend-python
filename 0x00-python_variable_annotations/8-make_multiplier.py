#!/usr/bin/env python3
"""annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier"""
    def func(x: float) -> float:
        """ returns a function that multiplies a float by multiplier"""
        return x * multiplier
    return func

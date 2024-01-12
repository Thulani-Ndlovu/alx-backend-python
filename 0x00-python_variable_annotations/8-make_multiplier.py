#!/usr/bin/env python3
'''Function that takes a float and returns a function that takes a float'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns function that multiplies a float by multiplier'''
    return lambda tmp: tmp * multiplier

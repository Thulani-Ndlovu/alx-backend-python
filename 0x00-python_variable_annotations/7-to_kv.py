#!/usr/bin/env python3
'''Function that returns a tuple from a str and int or float'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuple of k and v elements'''
    return (k, v**2)

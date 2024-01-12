#!/usr/bin/env python3
'''Sum items in a type annotated list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns sum of a list'''
    return sum(input_list)

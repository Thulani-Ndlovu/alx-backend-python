#!/usr/bin/env python3
'''Sums a list of mixed list items of int and float'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of all elements in mxd_lst as a float.'''
    return sum(mxd_lst)

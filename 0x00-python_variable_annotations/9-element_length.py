#!/usr/bin/env python3
'''Annotates the functions' parameters'''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return values with the appropriate types'''
    return [(i, len(i)) for i in lst]

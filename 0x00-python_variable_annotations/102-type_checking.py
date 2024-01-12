#!/usr/bin/env python3
'''Validating code using mypy'''
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
        Uses mypy to validate the following piece
        of code and apply any necessary changes.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)

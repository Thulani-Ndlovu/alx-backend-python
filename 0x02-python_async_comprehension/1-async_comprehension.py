#!/usr/bin/env python3
'''async_comprehension function'''
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns 10 random numbers'''
    return [i async for i in async_generator()]

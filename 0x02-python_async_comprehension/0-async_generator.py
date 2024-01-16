#!/usr/bin/env python3
'''async_generator coroutine'''
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    '''Yields a random  number between 0 - 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

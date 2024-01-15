#!/usr/bin/env python3
'''asynchronous coroutine function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for random delay between 0 and max_delay seconds.'''
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time

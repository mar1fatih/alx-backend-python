#!/usr/bin/env python3
"""async function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spawns wait_random n times with the specified max_delay'''
    i: int
    tasks: List[float] = []
    lists: List[float] = []
    for i in range(0, n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        lists.append(await task)
    return lists

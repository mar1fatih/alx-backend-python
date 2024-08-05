#!/usr/bin/env python3
"""async function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calls task_wait_random n times"""
    i: int
    tasks: List[float] = []
    lists: List[float] = []
    for i in range(0, n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        lists.append(await task)
    return lists

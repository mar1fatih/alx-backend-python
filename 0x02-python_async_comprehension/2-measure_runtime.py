#!/usr/bin/env python3
"""async function"""
import asyncio
from typing import List
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runtime of calling async_comprehension 4 times"""
    tm: float = time()
    tasks: List[float] = []
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    tm = time() - tm
    return tm

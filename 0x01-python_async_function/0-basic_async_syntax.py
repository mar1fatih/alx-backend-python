#!/usr/bin/env python3
"""async function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function that waits a random time"""
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

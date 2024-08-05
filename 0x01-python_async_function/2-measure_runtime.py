#!/usr/bin/env python3
"""async function"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measuring the runtime of wait_n"""
    temps: float = time()
    asyncio.run(wait_n(n, max_delay))
    temps = time() - temps
    return temps/n

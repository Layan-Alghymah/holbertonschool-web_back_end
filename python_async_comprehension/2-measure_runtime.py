#!/usr/bin/env python3
"""Measure the execution time of four concurrent async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel comprehensions."""
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.time() - start_time

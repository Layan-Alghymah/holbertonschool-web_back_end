#!/usr/bin/env python3
"""Measure the runtime of concurrent asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Return the time taken to run four async comprehensions concurrently."""
    start = time.perf_counter()

    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    return time.perf_counter() - start

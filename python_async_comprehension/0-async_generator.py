#!/usr/bin/env python3
"""This module defines an asynchronous random number generator."""

import asyncio
import random


async def async_generator():
    """Generate ten random numbers asynchronously, one per second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

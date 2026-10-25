#!/usr/bin/env python3
"""Create an asyncio Task for a random delay."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Schedule wait_random as an asyncio Task and return it."""
    return asyncio.create_task(wait_random(max_delay))

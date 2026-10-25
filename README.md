
# Python - Async

## Description
This project introduces asynchronous programming in Python using `asyncio`. It focuses on writing coroutines, running multiple tasks concurrently, and measuring execution time.

## Learning Objectives
- Understand `async` and `await`.
- Write and execute asynchronous coroutines.
- Run multiple coroutines concurrently.
- Create tasks using `asyncio.create_task()`.
- Measure asynchronous execution time.
- Generate random delays using `random.uniform()`.

## Requirements
- Python 3.8
- Ubuntu 20.04 LTS
- pycodestyle 2.5.x

## Files

| File | Description |
|------|-------------|
| `0-basic_async_syntax.py` | Wait for a random delay using a coroutine. |
| `1-concurrent_coroutines.py` | Execute multiple coroutines concurrently. |
| `2-measure_runtime.py` | Measure the total execution time. |
| `3-tasks.py` | Create an asyncio task. |
| `4-tasks.py` | Execute multiple tasks concurrently. |

## Usage

Run a Python test file:

```bash
python3 0-main.py
```

## Key Concepts
- **Coroutine:** A function defined using `async def`.
- **await:** Pauses a coroutine while waiting for an operation.
- **asyncio:** Python library for asynchronous programming.
- **Task:** Schedules a coroutine to run concurrently.

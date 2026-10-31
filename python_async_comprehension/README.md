# Python - Async Comprehension

## Description
This project explores asynchronous generators, asynchronous comprehensions, and concurrent execution in Python using the `asyncio` module.

## Learning Objectives
- Understand how to write asynchronous generators.
- Use asynchronous comprehensions to collect generated values.
- Apply type annotations to asynchronous generators.
- Execute multiple asynchronous operations concurrently.
- Measure the runtime of concurrent asynchronous tasks.

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8
- pycodestyle 2.5.x
- All Python files must be executable.
- All modules and functions must include documentation.
- All functions and coroutines must have type annotations.

## Tasks

### 0. Async Generator
Implement an asynchronous generator that yields 10 random floating-point numbers between 0 and 10, waiting one second between each value.

**File:** `0-async_generator.py`

### 1. Async Comprehensions
Use an asynchronous comprehension to collect 10 random numbers from the asynchronous generator.

**File:** `1-async_comprehension.py`

### 2. Run Time for Four Parallel Comprehensions
Execute four asynchronous comprehensions concurrently using `asyncio.gather()` and measure their total execution time.

**File:** `2-measure_runtime.py`

## Repository
- **GitHub Repository:** `holbertonschool-web_back_end`
- **Directory:** `python_async_comprehension`

#!/usr/bin/env python3
"async basics"
import time
from asyncio import run

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    "measure time a function takes"
    time1 = time.time()
    x = run(wait_n(n, max_delay))
    total_time = time.time() - time1
    return total_time / n

#!/usr/bin/env python3
"basics of async"
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    "returning the range of numbers based on input"

    value = random.uniform(0, max_delay)
    asyncio.sleep(value)
    return value

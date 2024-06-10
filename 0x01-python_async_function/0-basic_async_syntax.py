#!/usr/bin/env python3
import random

"basics of async"


async def wait_random(max_delay: int = 10):
    "returning the range of numbers based on input"
    return random.uniform(0, max_delay)

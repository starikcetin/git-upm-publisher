import os
import time
import asyncio

async def for_file(path_to_file, check_period):
    while not os.path.exists(path_to_file):
        await asyncio.sleep(check_period)
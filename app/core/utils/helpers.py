from typing import Callable, Any

import asyncio
import re


async def run_in_thread(func: Callable, *args: Any, **kwargs: Any) -> Any:
    """
    Run a blocking function in a separate thread asynchronously.
    """

    return await asyncio.to_thread(func, *args, **kwargs)
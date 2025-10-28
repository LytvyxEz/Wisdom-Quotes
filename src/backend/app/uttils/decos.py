import asyncio

from functools import wraps
from typing import Callable, Coroutine


def try_except(func: Callable | Coroutine) -> Callable | Coroutine:
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                return str(e)
        return async_wrapper
    else:
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return str(e)
        return sync_wrapper
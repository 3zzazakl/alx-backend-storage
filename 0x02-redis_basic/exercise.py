#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import uuid
from typing import Optional, Union, Callable
from functools import wraps
import redis


def call_history(method: Callable) -> Callable:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        meth_name = method.__qualname__
        self._redis.rpush(meth_name + ":inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(meth_name + ":outputs", output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """summary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    meth_name = method.__qualname__
    redis_db = method.__self__._redis
    inputs = redis_db.lrange(meth_name + ":inputs", 0, -1)
    outputs = redis_db.lrange(meth_name + ":outputs", 0, -1)

    print(f"{meth_name} was called {len(inputs)} times:")
    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print(f"{meth_name}(*{input}) -> {output}")


def count_calls(method: Callable) -> Callable:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self) -> None:
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None,
            ) -> Union[str, bytes, int, float, None]:
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            value = fn(value)
        return value

    def get_int(self, key: str) -> Union[int, None]:
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.get(key, int)

    def get_str(self, key: str) -> Union[str, None]:
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.get(key, str)

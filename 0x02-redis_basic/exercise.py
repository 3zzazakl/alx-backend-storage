#!/usr/bin/env python3
"""
Exercise file
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class
    """
    def __init__(self):
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> Union[
        str, bytes, int, float, None]:
        """
        Get data from cache
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """
        Get data from cache as string
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Get data from cache as integer
        """
        return self.get(key, fn=int)

#!/usr/bin/env python3

"""
This module contains code for interfacing
with redis via a python client
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """keeps track of the amount of times
    a function is called
    """

    @wraps(method)
    def wrapper(*args, **kwds):
        """keeps track of the amount of times
                a function is called
        """
        _redis: redis.Redis = args[0]._redis
        _redis.incr(method.__qualname__)

        return method(*args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """keeps track of the amount of the output and
    input that method was called with
    """

    @wraps(method)
    def wrapper(*args, **kwds):
        """keeps track of the amount of the output and
         input that method was called with
        """
        _redis: redis.Redis = args[0]._redis

        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        inputs = str(args[1:])
        output = method(*args, **kwds)

        _redis.rpush(input_key, inputs)
        _redis.rpush(output_key, output)

        return output

    return wrapper


class Cache:
    """This class uses redis as a
    cache store
    """

    def __init__(self) -> None:
        """
        constructor to initialise
        redis instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores some data in redis and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Union[Callable, None] = None) -> Union[str,
                                                       bytes, int,
                                                       float, None]:
        """Retrieve stored data via a  key
        """

        data = self._redis.get(key)

        if fn is None or data is None:
            return data

        return fn(data)

    def get_str(self, key: str) -> Union[str, None]:
        """Automatically parametrizes get with
        the the str conversion function
        """

        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Automatically parametrizes get with
        the the int conversion function
        """

        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """display the history of calls of a
    particular function"""
    _redis = redis.Redis()
    method_name = method.__qualname__

    input_key = "{}:inputs".format(method_name)
    output_key = "{}:outputs".format(method_name)

    inputs = _redis.lrange(input_key, 0, -1)
    outputs = _redis.lrange(output_key, 0, -1)

    print("{} was called {} times:".format(method_name, len(inputs)))

    for io in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name,
              io[0].decode(), io[1].decode()))

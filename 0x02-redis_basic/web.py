#!/usr/bin/env python3

"""
This module contains code for interfacing
with redis via a python client
"""

import redis
import requests


def get_page(url: str) -> str:
    """It uses the requests module to obtain
    the HTML content of a particular URL and returns it.
    """

    _redis = redis.Redis()

    # Check cache for url
    data = _redis.get(url)

    # Fetch and cache data
    if data is None:
        response = requests.get(url)
        data = response.content
        _redis.setex(url, 10, data)

    # Update number of calls
    _redis.incr("count:{}".format(url))

    return data.decode()

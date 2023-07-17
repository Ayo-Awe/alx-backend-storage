#!/usr/bin/env python3

"""Python to mongodb scripts
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a document into
    a collection
    """

    res = mongo_collection.insert_one(kwargs)

    return res.inserted_id

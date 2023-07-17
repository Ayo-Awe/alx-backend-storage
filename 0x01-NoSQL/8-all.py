#!/usr/bin/env python3

"""Python to mongodb scripts
"""


def list_all(mongo_collection):
    """Lists all documents in a mongo
    collection
    """
    res = []

    for doc in mongo_collection.find():
        res.append(doc)

    return res

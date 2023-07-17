#!/usr/bin/env python3

"""Python to mongodb scripts
"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a document based on
    a given name
    """

    res = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})

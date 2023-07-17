#!/usr/bin/env python3

"""Python to mongodb scripts
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic
    """

    res = []
    cursor = mongo_collection.find({"topics": topic})
    for doc in cursor:
        res.append(doc)

    return res

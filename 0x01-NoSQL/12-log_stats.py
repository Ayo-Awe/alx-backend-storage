#!/usr/bin/env python3

"""Python to mongodb scripts
"""
from pymongo import MongoClient


def main():
    """queries a collection, formats its data
    and prints it to stdout
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    count = nginx_collection.count()
    status_checks = nginx_collection.count(
        {"path": "/status", "method": "GET"})
    cursor = nginx_collection.aggregate(
        [{"$group": {"_id": "$method", "count": {"$count": {}}}}])

    method_agg = [data for data in cursor]
    methods = format_method_aggregates(method_agg)

    print("{} logs".format(count))
    print("Methods:\n" + '\n'.join(["\tmethod {}: {}".format(obj["method"], obj["count"])
          for obj in methods]))
    print("{} status check".format(status_checks))


def format_method_aggregates(aggregates):
    """reformat aggregated data
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    res = []

    for method in methods:
        count = 0

        for agg in aggregates:
            if agg["_id"] == method:
                count = agg["count"]
                break

        res.append({"method": method, "count": count})

    return res


if __name__ == "__main__":
    main()

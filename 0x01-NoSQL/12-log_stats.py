#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from pymongo import MongoClient


def log_stats():
    """ log stats """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    count = logs_collection.count_documents({})
    print("{} logs".format(count))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        meth_count = logs_collection.count_documents({"method": method})
        print("\tmethod: {}: {}".format(method, meth_count))

    status_checks = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check".format(status_checks))


if __name__ == "__main__":
    log_stats()

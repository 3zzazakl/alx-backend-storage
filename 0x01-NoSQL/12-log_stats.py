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

    db = client.my_db
    school_collection = db.school

    total_logs = school_collection.count_documents({})

    methods = {"GET", "POST", "PUT", "DELETE", "PATCH"}
    methods_counts = {}
    for method in methods:
        methods_counts[method] = school_collection.count_documents({
            "method": method})

    status_check = school_collection.count_documents({
        "method": "GET",
        "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_counts[method]}")

    print(f"{status_check} status checks")


if __name__ == "__main__":
    log_stats()

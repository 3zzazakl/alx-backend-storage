#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from pymongo import MongoClient


def log_stats():
    """ log stats """
    client = MongoClient()

    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})

    status_count = nginx_collection.aggregate([
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
        ])

    print(f"{total_logs} logs")
    print("Methods:")

    methods_counts = nginx_collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
        ])

    methods = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "PATCH": 0}
    for method in methods_counts:
        if method['_id'] in methods:
            methods[method['_id']] = method['count']

    for method, count in methods.items():
        print(f"\tmethod {method}: {count}")

    status_codes = {}
    for status in status_count:
        status_codes[status['_id']] = status['count']

    print(f"{sum(status_codes.values())} status checks")

    for status_code, count in status_codes.items():
        print(f"\tstatus {status_code}: {count}")

    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count":
        {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']} => {ip['count']}")


if __name__ == "__main__":
    log_stats()

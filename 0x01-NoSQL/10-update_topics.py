#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def update_topics(mongo_collection, name, topics):
    """ update topics """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})

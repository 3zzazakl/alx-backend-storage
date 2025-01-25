#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def update_topics(mongo_collection, name, topics):
    """ update topics """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

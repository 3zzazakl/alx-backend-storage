#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def schools_by_topic(mongo_collection, topic):
    """ schools by topic """
    return mongo_collection.find({"topics": topic})

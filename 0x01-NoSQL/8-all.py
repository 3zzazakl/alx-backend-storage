#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def list_all(mongo_collection):
    """ list all documents """
    return mongo_collection.find()

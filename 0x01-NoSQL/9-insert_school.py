#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def insert_school(mongo_collection, **kwargs):
    """ insert document """
    school = mongo_collection.insert_one(kwargs)
    return school.inserted_id

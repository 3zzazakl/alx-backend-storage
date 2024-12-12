#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def top_students(mongo_collection):
    """ top students """
    students = mongo_collection.find()

    result = []

    for student in students:
        topics = student.get('topics', [])
        total_score = sum([topic['score'] for topic in topics])
        average_score = total_score / len(topics) if topics else 0

        student['averageScore'] = average_score
        result.append(student)

    result.sort(key=lambda student: student['averageScore'], reverse=True)

    return result

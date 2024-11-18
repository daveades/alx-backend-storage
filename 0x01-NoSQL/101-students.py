#!/usr/bin/env python3
"""
Advanced task 1
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    :param mongo_collection: The pymongo collection object
    :return: List of students with averageScore included
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$scores"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))

    return result


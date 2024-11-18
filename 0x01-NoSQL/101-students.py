#!/usr/bin/env python3
"""
Advanced task 1
"""


def top_students(mongo_collection):
	"""
	Returns all students sorted by average scores
	"""

	pipeline = [
		{
			'$project': {
				'_id': 1,
				'name': 1,
				'averageScore': {
					'$avg': '$topics.score',
				},
				'topics': 1,
			},
		},
		{
			'$sort': {'averageScore': -1},
		},
	]

	result = list(mongo_collection.aggregate(pipeline))

	return result

#!/usr/bin/env python3
"""Task 10"""

def update_topics(mongo_collcetion, name, topics):
	"""
	Update topics of documents in a collection based on name
	"""
	mongo_collection.update_many(
			{'name': name},
			{'$set': {'topics': topics}}
	)

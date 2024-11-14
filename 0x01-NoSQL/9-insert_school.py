#!/usr/bin/env python3

"""
Module that contains function to
insert a new doc in a mongo collection
"""

def insert_School(mongo_collection, **kwargs):
	"""
	Function to insert a new document
	in a collection based on **kwargs
	"""
	insertion_result = mongo_collection.insert_one(kwargs)
	return insertion_result.inserted_id


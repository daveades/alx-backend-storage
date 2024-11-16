#!/usr/bin/env python3
"""
Task 11
"""

def schools_by_topic(mongo_collection, topic):
	"""
	Function that returns the list of school having a specific topic
	"""
	schools_filter = {
		'topics': {
			'$elemMatch': {
				'$eq': topic,
			},
		},
	}
	
	schools_list = [school_doc for school_doc in mongo_collection.find(school_filter)]
	return schools_list

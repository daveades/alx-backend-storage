#!/usr/bin/env python3
"""
Module that holds the function 
to list all list all documents in a collection 
"""


def list_all(mongo_collection):
	"""
	Lists all documents in a collection
	"""
	doc_list = [doc for doc in mongo_collection.find()]
	return doc_list

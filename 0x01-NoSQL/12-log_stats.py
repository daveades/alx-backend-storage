#!/usr/bin/env python3

"""
Task 12
"""

from pymongo import MongoClient

def get_stats(nginx_collection):
	"""
	Retrieves the stats from the nginx log stored in the database
	"""
	# total number of logs
	total_logs = nginx_collection.count_documents({})

	# count documents for each method
	methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
	method_counts = {
		method: nginx_collection.count_documents(
					{
						'method': method
					}
		) for method in methods
	}
	
	# count documents with method='GET' and path='/status'
	status_check_count = nginx_collection.count_documents(
			{
				'method': 'GET',
				'path': '/status'
			}
	)
	
	return total_logs, method_counts, status_check_count

def main():
	"""
	Main function to display log stats
	"""
	# connect to mongoDB
	client = MongoClient('mongodb://localhost:27017')
	
	# Retrieve the info from the get_stats func.
	total_logs, method_counts, status_check_count = get_stats(client.logs.nginx)

	# Display stats
	print(f"{total_logs} logs")
	print('Methods:')
	for method, count in method_counts.items():
		print(f'\tmethod {method}: {count}')
	print(f'{status_check_count} status check')


if __name__ == '__main__':
	main()


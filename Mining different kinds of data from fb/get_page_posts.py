# import os
# import json
# from argparse import ArgumentParser
# import facebook
# import requests

# def get_parser():
# 	parser = ArgumentParser()
# 	parser.add_argument('--page')
# 	parser.add_argument('--n', default=100, type=int)
# 	return parser

# if __name__ == '__main__':
# 	parser = get_parser()
# 	args = parser.parse_args()

# 	token = 'EAANcgmchBvsBAEa65LtJIGWK9ouL6V8IsGQHcOkTB3QizSTD0KtCI6jBZCZBvvYLnd4UrNOnwBUop1rqWQ0UEp6hNd3myZC6GljtXCgBQobZBZBrSXLIiI4ZATUPvLFn138JCHDLwD7hpZAmBRpGR01eZBKRPCzZBIkkayOhUODEPagAKZAFHeUA9YH2C7ZC5Ck3Rmktxo7LeEohQZDZD'

# 	graph = facebook.GraphAPI(token, version=3.0)
# 	all_fields = [
# 	'id',
# 	'message',
# 	'created_time',
# 	'shares',
# 	'likes.summary(true)',
# 	'comments.summary(true)',
# 	'reactions'
# 	]
# 	all_fields = ','.join(all_fields)
# 	posts = graph.get_connections('PacktPub', 'posts', fields=all_fields)
# 	downloaded = 0
# 	while True: # keep paginating
# 		if downloaded >= args.n:
# 			break
# 		try:
# 			fname = 'posts_{}.jsonl'.format(args.page)
# 			with open(fname, 'a') as f:
# 				for post in posts['data']:
# 					downloaded += 1
# 					f.write(json.dumps(post)+"\n")
# 				# get next page
# 				posts = requests.get(posts['paging']['next']).json()
# 		except KeyError:
# 			# no more pages, break the loop
# 			break

import os
import json
from argparse import ArgumentParser
import facebook
import requests

def get_parser():
	parser = ArgumentParser() # To take page name from command line
	parser.add_argument('--page')
	parser.add_argument('--n', default=100, type=int)
	return parser

if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()

	token = 'EAANcgmchBvsBAL43EBt8mafG5pc7szkU5001lPubWrggFUxySOmbQRZAhzXpMkJgFEYhk0AzZBZBPU5ciIVJHXevI8YcxZBUB7XtXskvUETXZA3RunIaTf3swPU8mVVCyEJEJpLWf1Syxyqe8ZCnK35VzYHzaDVc1Fqvwz78nIi6ZC5ZCnOYauDVV9mqC7dwnC1DUqETB86jaYRb4tOSSKWmARL5vSG0UHZBlsTSMa8hZBUwZDZD'
	graph = facebook.GraphAPI(token, version=3.1)
	all_fields = [
	'id',
	'message',
	'created_time',
	'shares',
	'likes.summary(true)', # to check the no. of times the post's been liked/shared/commented
	'comments.summary(true)', # true is to get statistics, that's count
	'reactions'
	]
	all_fields = ','.join(all_fields)
	posts = graph.get_connections('teensMania', 'posts', fields=all_fields)
	downloaded = 0
	while True: # keep paginating
		if downloaded >= args.n:
			break
		try:
			fname = 'posts_{}.jsonl'.format(args.page)
			with open(fname, 'a') as f:
				for post in posts['data']:
					downloaded += 1
					f.write(json.dumps(post)+"\n")
				# get next page
				posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			# no more pages, break the loop
			break
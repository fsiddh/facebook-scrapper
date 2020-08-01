import os
import json
from argparse import ArgumentParser
import facebook
import requests

def get_parser():
	parser = ArgumentParser()
	parser.add_argument('--page')
	parser.add_argument('--n', default=100, type=int)
	return parser

if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()

	token = 'EAANcgmchBvsBAByxcHHnZChe0jXeTZCcxZArqaIWAsbgCZBACCK10SM9bMWMIX0NYUnkqTDGjFrZAQpgK3XeJejPNtBnv60IpEDWmTXHfZA2DrIbhLa4xbTCPZBsiUU9KI0A8ZCERfCdxIEWbNzFL788nQ76NId9rLyGIZAjyXgZBNaVUsQXPngbcT2sTsyGXwyDBITAYmioWrvwZDZD'

	graph = facebook.GraphAPI(token, version=2.7)
	all_fields = [
	'id',
	'message',
	'created_time',
	'shares',
	'likes.summary(true)',
	'comments.summary(true)',
	'reactions'
	]
	all_fields = ','.join(all_fields)
	posts = graph.get_connections('PacktPub', 'posts', fields=all_fields)
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


#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import json
import facebook
import requests

if __name__ == '__main__':
	token = 'EAANcgmchBvsBAByxcHHnZChe0jXeTZCcxZArqaIWAsbgCZBACCK10SM9bMWMIX0NYUnkqTDGjFrZAQpgK3XeJejPNtBnv60IpEDWmTXHfZA2DrIbhLa4xbTCPZBsiUU9KI0A8ZCERfCdxIEWbNzFL788nQ76NId9rLyGIZAjyXgZBNaVUsQXPngbcT2sTsyGXwyDBITAYmioWrvwZDZD'

	graph = facebook.GraphAPI(token)
	all_fields = [
	'message',
	'created_time',
	'description',
	'caption',
	'link',
	'place',
	'status_type'
	]
	all_fields = ','.join(all_fields)
	posts = graph.get_connections('me', 'posts', fields=all_fields)

	while True: # keep paginating
		try:
			with open('my_posts2.jsonl', 'a') as f:
				for post in posts['data']:
					f.write(json.dumps(post)+"\n")
				# get next page
				posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			# no more pages, break the loop
			break
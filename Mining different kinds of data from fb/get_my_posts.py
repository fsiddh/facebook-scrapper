#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import json
import facebook
import requests

if __name__ == '__main__':
	token = 'EAANcgmchBvsBAHY1sRrrEC8eFcZAfTW6QOGZAzBJHZCT9QFG8Wo7lufbb2ZA4Kn18gxBEwDjiRA4EVITQ4os6bitTdeqvNkORwvGforgh8vNimft1b6SwYrwnYZAq28EU0KW0zh2pJi8h8kUAkMZClaQMsKUoIz3GYNxBnZAc1HEX5PfBdkEd0X5XjBVMsQnETdwnjRKqagZBbazupIjcZBtJcWoACRmHiYzcfxvqHZBdMyQZDZD'

	graph = facebook.GraphAPI(token)
	posts = graph.get_connections('me', 'posts')

	while True: # keep paginating
		try:
			with open('my_posts.jsonl', 'a') as f:
				for post in posts['data']:
					f.write(json.dumps(post)+"\n")
				# get next page
				posts = requests.get(posts['paging']['next']).json()
		except KeyError:
			# no more pages, break the loop
			break

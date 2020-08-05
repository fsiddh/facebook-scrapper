#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import facebook
import json

if __name__ == '__main__':
	token = 'EAANcgmchBvsBAHY1sRrrEC8eFcZAfTW6QOGZAzBJHZCT9QFG8Wo7lufbb2ZA4Kn18gxBEwDjiRA4EVITQ4os6bitTdeqvNkORwvGforgh8vNimft1b6SwYrwnYZAq28EU0KW0zh2pJi8h8kUAkMZClaQMsKUoIz3GYNxBnZAc1HEX5PfBdkEd0X5XjBVMsQnETdwnjRKqagZBbazupIjcZBtJcWoACRmHiYzcfxvqHZBdMyQZDZD'

	graph = facebook.GraphAPI(token)
	user = graph.get_object("me")
	friends = graph.get_connections(user["id"], "friends")
	print(json.dumps(friends, indent=4))
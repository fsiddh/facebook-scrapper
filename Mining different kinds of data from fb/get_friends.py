#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import facebook
import json

if __name__ == '__main__':
	token = 'EAANcgmchBvsBAByxcHHnZChe0jXeTZCcxZArqaIWAsbgCZBACCK10SM9bMWMIX0NYUnkqTDGjFrZAQpgK3XeJejPNtBnv60IpEDWmTXHfZA2DrIbhLa4xbTCPZBsiUU9KI0A8ZCERfCdxIEWbNzFL788nQ76NId9rLyGIZAjyXgZBNaVUsQXPngbcT2sTsyGXwyDBITAYmioWrvwZDZD'

	graph = facebook.GraphAPI(token)
	user = graph.get_object("me")
	friends = graph.get_connections(user["id"], "friends")
	print(json.dumps(friends, indent=4))
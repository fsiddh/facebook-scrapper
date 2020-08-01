#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import json
import facebook

if __name__ == '__main__':
	token = 'EAANcgmchBvsBAByxcHHnZChe0jXeTZCcxZArqaIWAsbgCZBACCK10SM9bMWMIX0NYUnkqTDGjFrZAQpgK3XeJejPNtBnv60IpEDWmTXHfZA2DrIbhLa4xbTCPZBsiUU9KI0A8ZCERfCdxIEWbNzFL788nQ76NId9rLyGIZAjyXgZBNaVUsQXPngbcT2sTsyGXwyDBITAYmioWrvwZDZD'

	graph = facebook.GraphAPI(token)
	profile = graph.get_object('me', fields='name,location{location}')

	print(json.dumps(profile, indent=4))
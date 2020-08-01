import os
import json
import facebook
from argparse import ArgumentParser

def get_parser():
	parser = ArgumentParser()
	parser.add_argument('--page')
	return parser

if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()

	token = 'EAANcgmchBvsBAByxcHHnZChe0jXeTZCcxZArqaIWAsbgCZBACCK10SM9bMWMIX0NYUnkqTDGjFrZAQpgK3XeJejPNtBnv60IpEDWmTXHfZA2DrIbhLa4xbTCPZBsiUU9KI0A8ZCERfCdxIEWbNzFL788nQ76NId9rLyGIZAjyXgZBNaVUsQXPngbcT2sTsyGXwyDBITAYmioWrvwZDZD'
	fields = ['id',
		'name',
		'about',
		'likes',
		'website',
		'link'
		]
	fields = ','.join(fields)

	graph = facebook.GraphAPI(token, version=3.1)
	page = graph.get_object(args.page, fields=fields)

	print(json.dumps(page, indent=4))
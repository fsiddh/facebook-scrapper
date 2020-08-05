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

	token = 'EAANcgmchBvsBAEa65LtJIGWK9ouL6V8IsGQHcOkTB3QizSTD0KtCI6jBZCZBvvYLnd4UrNOnwBUop1rqWQ0UEp6hNd3myZC6GljtXCgBQobZBZBrSXLIiI4ZATUPvLFn138JCHDLwD7hpZAmBRpGR01eZBKRPCzZBIkkayOhUODEPagAKZAFHeUA9YH2C7ZC5Ck3Rmktxo7LeEohQZDZD'
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
#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import facebook
import json

if __name__ == '__main__':
	token = 'EAANcgmchBvsBACHZAxQKmaNVhRzNK5flowL1NMzQSjvUkrEEORgGwuL23pcY5sco0KmZBVLUi3eBKpwbIdHopL3LNJHC5EDE3aabltkbadSQcpOXQZAxS4gKIZCHrkq12DzPJXSrfMdcZAByA7ZBOeWKVlZClHIcnrEGc819uzjqTYV14jZCTEfeIJmPRnKoZAIIFqB1Y0urQ1tSfgLGRXftSaN1CRLvAUWfpZCGcc1uweBwZDZD'

	graph = facebook.GraphAPI(token)
	user = graph.get_object("me")
	friends = graph.get_connections(user["id"], "friends")
	print(json.dumps(friends, indent=4))
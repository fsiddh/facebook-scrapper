#Source Code for Mining data on Facebook with Python Course by TigerStyle Code Academy 

import os
import json
import facebook

if __name__ == '__main__':
	token = 'EAANcgmchBvsBAAqYdkAUwScmQLWNZAPsn3UidWPQbpCLMdqZAItlmDJpcVhu0x8ZBRunByJ0HGmJrxDdTEUYvaT1zCfALlSVH1VREHWyTZBl9POQutW6PfZCB8mEWTudOcREDN2QCkPMhBmSMIzJduuKWO5RZAfiZCU5rIJMkPHSF8IHQB66ZCq4zDeagfZA4As2sxa4ty7PMrAZDZD'

	graph = facebook.GraphAPI(token)
	profile = graph.get_object('me', fields='name,location{location}')

	print(json.dumps(profile, indent=4))
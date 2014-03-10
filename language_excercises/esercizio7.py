import requests
import json

resp = requests.get("http://ialpython.apiary.io/people")
email = json.loads(resp.content)




name = {}
for k,v in email:
	name[v] = k
print name
	
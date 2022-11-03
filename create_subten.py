import requests
from morpheuscypher import Cypher

api_key = Cypher(morpheus=morpheus, ssl_verify=False).get('secret/pw_api_key:api_key')
url = 'https://cloudkey.corp.gipnetworks.com/api/accounts'

headers = {
    "accept": "application/json",
    "tontent-type": "application/json",
    "authorization": f"Bearer {api_key}"
}

response = requests.post(url, headers=headers)

print(response.text)




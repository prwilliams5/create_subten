import requests

api_key = morpheus['morpheus']['apiAccessToken']
url = 'https://cloudkey.corp.gipnetworks.com/api/accounts'

subten_name = morpheus['customOptions']['subtenName']

headers = {
    "accept": "application/json",
    "tontent-type": "application/json",
    "authorization": f"Bearer {api_key}"
}

payload = {
    "account": {
        "currency": "USD",
        "name": subten_name
    }
}

response = requests.post(url, headers=headers, verify=False)

print(response.text)




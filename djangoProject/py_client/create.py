import requests

endpoint = "http://localhost:8000/api/products/"

data = {
	'title': 'Tru Tien',
	'price' : 12
}

print (data)

get_response = requests.get(endpoint)

print(get_response.json())

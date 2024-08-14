import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint) # HTTP Request

#print(get_response.text) # print raw text response
# print(get_response.json())

print(get_response.json())

# HTTP Request -> HTTP
# REST API HTTP Requst -> JSON(YML)
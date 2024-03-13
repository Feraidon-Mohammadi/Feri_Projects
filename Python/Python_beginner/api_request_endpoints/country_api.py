import requests

url = "https://ajayakv-rest-countries-v1.p.rapidapi.com/rest/v1/all"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "ajayakv-rest-countries-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())





################################################  HTTP api #########################################################
import http.client

conn = http.client.HTTPSConnection("ajayakv-rest-countries-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "ajayakv-rest-countries-v1.p.rapidapi.com"
}

conn.request("GET", "/rest/v1/all", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



######################################################################### another -####################
import requests

url = "https://countryapi.io/api/all"

payload={}
headers = {
  'Authorization': 'YOUR-APIKEY',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
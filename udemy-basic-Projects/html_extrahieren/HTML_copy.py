import requests


# get html codes

url = "https://www.yasdl.com/"


response = requests.get(url)
if response.status_code==200:
	print(response.text)
	



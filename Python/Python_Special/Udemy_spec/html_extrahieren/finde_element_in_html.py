import requests
from bs4 import BeautifulSoup

url = "https://www.yasdl.com/"
response = requests.get(url)
if response.status_code == 200:
	doc = BeautifulSoup(response.text, "html.parser")
	
	finders = doc.find_all("img")
	# for finder in finders:
	# 	element = "img"
	# 	if "name" in finders and "name" == element:
	# 		print(finders)
	
	print(finders)

# print(doc.find("name"))


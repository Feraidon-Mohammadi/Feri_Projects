# import urllib.parse
# import requests
# from bs4 import BeautifulSoup
#
#
#
# url = "https://example.com"
# response = requests.get(url)
#
# found_images = []
# if response.status_code == 200:
# 	doc = BeautifulSoup(response.text, "html.parser")
#
# 	images = doc.find_all("img")
#
# 	for img in images:
# 		path = urllib.parse.urljoin(url, img.attrs["src"])
# 		found_images.append(path)
# 		print()
#
# ###########################################################
# import os
#
# if not os.path.exists("./images"):
# 	os.mkdir("./images")
#
# for found_image in found_images:
# 	file_name = found_image.split("/")[-1]
# 	response = requests.get(found_image)
#
# 	# wb  -> write in Binary
# 	with open("./images/" + file_name, "wb") as file:
# 		file.write(response.content)
#
		
	# --> this is for last line down ---> content because we want get bytes and index becuase we want
	# first 100 byete of the picture to get .because it take much time
	#print(response.content[:100])
	


##################################  gif downlaod #########################################################
import os
import urllib.parse
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"


pass1 = "password"
response = requests.get(url)

found_images = []
if response.status_code == 200:
	doc = BeautifulSoup(response.text, "html.parser")

	images = doc.find_all("img")

	for img in images:
		path = urllib.parse.urljoin(url, img.attrs["src"])
		found_images.append(path)

# Create a directory to save images
if not os.path.exists("./images"):
	os.mkdir("./images")

for found_image in found_images:
	file_name = found_image.split("/")[-1]
	response = requests.get(found_image)

	# Check if the image is a GIF (you can modify this condition based on your specific case)
	if file_name.lower().endswith(".gif"):
		with open("./images/" + file_name, "wb") as file:
			file.write(response.content)
			print(f"Downloaded: {file_name}")

###################### downnload picture with login  ##########################################
import urllib.parse
import requests
from bs4 import BeautifulSoup
import os

# url = "https://www.google.com"
# user= "username"
# user= "username"
# Add your login credentials

login_url = "https://www.googl.com/login" # example
login_payload = {
    'name': 'name',
    'username': 'username',
    'password': 'password'
}

# Perform login
session = requests.Session()
login_response = session.post(login_url, data=login_payload)

# Check if login was successful (you may need to adjust the condition based on the website's behavior)
if login_response.status_code == 200:
    # Continue with image scraping
    url = "https://www.example.com"
    response = session.get(url)

    found_images = []
    if response.status_code == 200:
        doc = BeautifulSoup(response.text, "html.parser")

        images = doc.find_all("img")

        for img in images:
            path = urllib.parse.urljoin(url, img.attrs["src"])
            found_images.append(path)
            print()

        # Create a directory for images if it doesn't exist
        if not os.path.exists("./images"):
            os.mkdir("./images")

        for found_image in found_images:
            file_name = found_image.split("/")[-1]
            response = session.get(found_image)

            # wb -> write in Binary
            with open("./images/" + file_name, "wb") as file:
                file.write(response.content)

            # --> this is for the last line down ---> content because we want to get bytes and index because we want
            # first 100 bytes of the picture to get because it takes much time
            # print(response.content[:100])
else:
    print("Login failed.")

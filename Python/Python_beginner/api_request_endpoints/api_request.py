import requests

# Make the API request
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")

#




data = response.json()

longitude= data["iss_position"]
print(longitude)
longitude1 = data["iss_position"]["longitude"]
print(longitude1)
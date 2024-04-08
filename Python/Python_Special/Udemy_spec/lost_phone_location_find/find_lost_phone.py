import requests

#
# def get_phone_location(phone_number):
#     url = f"https://api.example.com/location?phone={phone_number}"
#     url2 = f"https://notify.frankfurt.us1.twilio.com/v1?phone={phone_number}"
#     response = requests.get(url2)
#     data = response.json()
#     print(data)
#     return data["latitude"], data["longitude"]
#
# #phone = ""   {phone}
# phone_number = "+1234567890" #input(f"Enter your lost phone number: ")
# latitude, longitude = get_phone_location(phone_number)
# print("Phone Location:")
# print("Latitude:", latitude)
# print("Longitude:", longitude)

def get_phone_location(phone_number):
    # Use the correct URL based on your API endpoint
    url = f"https://api.example.com/location?phone={phone_number}"
    # Make sure to use the correct URL and handle the response appropriately
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Check the structure of the response to ensure correct key access
        if "latitude" in data and "longitude" in data:
            print(data)
            return data["latitude"], data["longitude"]
        else:
            print("Error: Unexpected response format")
    else:
        print(f"Error: Request failed with status code {response.status_code}")

# Example phone number (replace with user input if needed)
phone_number = "+49123456789"

try:
    latitude, longitude = get_phone_location(phone_number)
    print("Phone Location:")
    print("Latitude:", latitude)
    print("Longitude:", longitude)
except Exception as e:
    print(f"Error: {e}")


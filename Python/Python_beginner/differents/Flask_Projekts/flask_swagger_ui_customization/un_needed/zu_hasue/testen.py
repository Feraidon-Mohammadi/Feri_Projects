# testen
import secrets

# import requests
#
# url = "http://127.0.0.1:5000/auth"
# headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMjU5NDI0MSwianRpIjoiODFjOTM4MTMtYzkxMC00OTI5LWJlNTUtMzI5NWNiMTUxZjYzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZlcmkiLCJuYmYiOjE3MDI1OTQyNDEsImV4cCI6MTcwMjU5NTE0MX0.LHEVv5fMoA8ISsBaHn5BoUdBAizZSKlVsjKvYXhqt1k"}
#
# response = requests.get(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

########################################################################################################################
import requests
from flask import app
from flask_jwt_extended import create_access_token

url = "http://127.0.0.1:5000/auth"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMjU5NzEzOSwianRpIjoiYTI5ODdlNjAtNDdiMC00M2I2LThlYmYtMGIyMzhjODNlNTVhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZlcmkiLCJuYmYiOjE3MDI1OTcxMzksImV4cCI6MTcwMjU5ODAzOX0.5vfH1ipZlFvYiBu_q1P9Zyvk-SOb7gTA8UO0oLiXxU8"}

response = requests.get(url, headers=headers)

print(response.status_code)

try:
    # Try to parse the response as JSON
    json_content = response.json()
    print(json_content)
except ValueError:
    # If the response is not JSON, print the raw content
    print(response.text)



##################################################################################################
def token_required():
    user = {
        "id":1234,
        "name":"feri",
        "nachname":"moh"
    }

    new_secret_key = secrets.token_hex(32)
    access_token = create_access_token(identity=user)
    response_data = {
        "access_token":access_token,
        "message":"login successful"
    }
    print(response_data)
    return response_data


headers = {
    'Authorization': f'Bearer {token_required()["access_token"]}'
}

response = requests.get('https://127.0.0.1:5000/protected-route', headers=headers)
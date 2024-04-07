import requests

base_url = "http://127.0.0.1:5000/entities"


##################### login form with authentication without jwt ################
# url = "http://127.0.0.1:5000/login"
# auth = ("user", "password")
# response = requests.get(url, auth=auth)
# print(response.text)
#######################################################################################

# jwt json web token
url = "http://127.0.0.1:5000/protected"
token = "your-generated-jwt-token"
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(url, headers=headers)

print(response.text)


def get_entities():
    try:
        response_get = requests.get(base_url)
        response_get.raise_for_status()  # Raise an exception for HTTP errors
        return response_get.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")
        return None


def create_entity(data):
    try:
        response_post = requests.post(base_url, json=data)
        response_post.raise_for_status()  # Raise an exception for HTTP errors
        return response_post.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        return None


def update_entity(entity_id, data):
    try:
        response_put = requests.put(f"{base_url}/{entity_id}", json=data)
        response_put.raise_for_status()  # Raise an exception for HTTP errors
        return response_put.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during PUT request: {e}")
        return None


def delete_entity(entity_id):
    try:
        response_delete = requests.delete(f"{base_url}/{entity_id}")
        response_delete.raise_for_status()  # Raise an exception for HTTP errors
        return response_delete.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during DELETE request: {e}")
        return None


# base_url = "http://127.0.0.1:5000/entities"
#
#
# def get_entities():
#     response_get = requests.get(base_url)
#     return response_get.json()
#
#
# def create_entity(data):
#     response_post = requests.post(base_url, json=data)
#     return response_post.json()
#
#
# def update_entity(entity_id, data):
#     response_put = requests.put(f"{base_url}/{entity_id}", json=data)
#     return response_put.json()
#
#
# def delete_entity(entity_id):
#     response_delete = requests.delete(f"{base_url}/{entity_id}")
#     return response_delete.json()

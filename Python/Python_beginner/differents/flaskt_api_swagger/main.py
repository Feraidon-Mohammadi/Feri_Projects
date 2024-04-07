import requests
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
# from flask_restful_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import jwt
import datetime

app = Flask(__name__)
app.config['DEBUG'] = False  # turn off flask debuger
api = Api(app)


# Secret key for encoding and decoding JWT tokens
app.config['SECRET_KEY'] = 'your-secret-key'

entities_data = {
    "name": "feri",
    "age": 30,
    "gender": "Male",
    "address": {"country": "germany", "state": "koeln", "city": "rocky", "street": "michael_str_21", "plz": "24256"},
}


# Custom decorator for requiring JWT authentication
def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # Decode the token using the secret key
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return func(current_user, *args, **kwargs)

    return wrapper


class Entities(Resource):
    def get(self, entity_id=None):
        if entity_id is None:
            return entities_data
        else:
            if entity_id in entities_data:
                return {entity_id: entities_data[entity_id]}
            else:
                return {'error': f'Entity with ID {entity_id} not found'}, 404

    @token_required
    def post(self):
        parser = request.get_json()
        entity_id = len(entities_data) + 1
        entities_data[entity_id] = parser
        return {'id': entity_id, 'message': 'Entity created successfully'}

    @token_required
    def put(self, entity_id):
        if entity_id not in entities_data:
            return {'error': f'Entity with ID {entity_id} not found'}, 404

        parser = request.get_json()
        entities_data[entity_id] = parser
        return {'id': entity_id, 'message': 'Entity updated successfully'}

    @token_required
    def delete(self, entity_id):
        if entity_id not in entities_data:
            return {'error': f'Entity with ID {entity_id} not found'}, 404

        del entities_data[entity_id]
        return {'message': f'Entity with ID {entity_id} deleted successfully'}


api.add_resource(Entities, '/entities', '/entities/<int:entity_id>')

# Swagger configuration
swagger_url = '/swagger'
api_url = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': "Your API's Name"
    },
)
app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

# Generate Swagger JSON
api.add_resource(Resource, api_url, endpoint='swagger_json')

if __name__ == '__main__':
    try:
        # Your code here
        from urllib.request import something  # Example line
    except Exception as e:
        print(f"Error: {e}")
    
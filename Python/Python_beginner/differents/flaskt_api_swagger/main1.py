import requests
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, reqparse
import jwt
import datetime
# pip install flask-restfull
from flask_swagger_ui import get_swaggerui_blueprint
# pip install flask-swagger-ui
import check_version
from request_data import get_entities, create_entity, update_entity, delete_entity

app = Flask(__name__)
api = Api(app)


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
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return func(current_user, *args, **kwargs)

    return wrapper


# Secret key for encoding and decoding JWT tokens
app.config['SECRET_KEY'] = 'your-secret-key'


entities_data = {
    "name": "feri",
    "age": 30,
    "gender": "Male",
    "address": {"country": "germany", "state": "koeln", "city": "rocky", "street": "michael_str_21", "plz": "24256", }
}


@app.route('/')
def home():
    return 'Hello, Flask World!'


@app.route("/login")
def login():
    auth = request.authorization

    if auth and auth.username == "user" and auth.password == "password":
        # Generate a JWT token with the username and an expiration time
        token = jwt.encode(
            {'username': auth.username, 'exp': datetime.datetime.utcnow() +
             datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response("Could not verify!", 401, {"www-Authenticate": "Basic realm='login Required'"})


class Entities(Resource):

    def get(self, entity_id=None):
        if entity_id is None:
            return entities_data
        else:
            if entity_id in entities_data:
                return {entity_id: entities_data[entity_id]}
            else:
                return {'error': f'Entity with ID {entity_id} not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'key', type=str, help='Key for the entity', required=True)
        parser.add_argument('value', type=str,
                            help='Value for the entity', required=True)
        args = parser.parse_args()

        entity_id = len(entities_data) + 1
        entities_data[entity_id] = {'key': args['key'], 'value': args['value']}
        return {'id': entity_id, 'message': 'Entity created successfully'}

    def put(self, entity_id):
        if entity_id not in entities_data:
            return {'error': f'Entity with ID {entity_id} not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument(
            'key', type=str, help='Updated key for the entity', required=True)
        parser.add_argument('value', type=str,
                            help='Updated value for the entity', required=True)
        args = parser.parse_args()

        entities_data[entity_id] = {'key': args['key'], 'value': args['value']}
        return {'id': entity_id, 'message': 'Entity updated successfully'}

    def delete(self, entity_id):
        if entity_id not in entities_data:
            return {'error': f'Entity with ID {entity_id} not found'}, 404

        del entities_data[entity_id]
        return {'message': f'Entity with ID {entity_id} deleted successfully'}


api.add_resource(Entities, '/entities',
                 '/entities/<int:entity_id>', endpoint='entities')


###################################################
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
api.add_resource(Entities, api_url, endpoint='swagger_json')
# generate swager
api.add_resource(Entities, swagger_url, endpoint='swagger')

if __name__ == "__main__":
    app.run(debug=True)

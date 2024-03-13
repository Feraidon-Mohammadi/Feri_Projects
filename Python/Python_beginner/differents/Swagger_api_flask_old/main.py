import requests
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, fields
from flask_restx import  Resource, reqparse
# from flask_restful_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

import jwt
import datetime

app = Flask(__name__)
app.config['DEBUG'] = False  # turn off flask debuger
api = Api(app)

from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class Course(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	schulern = db.relationship("Schuler", back_populates="course")


class Schuler(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	course_id = db.Column(db.Integer, db.ForeignKey("course.id"))  # Foreign key linking to Course table

	course = db.relationship("Course", back_populates="schulern")


# Secret key for encoding and decoding JWT tokens
app.config['SECRET_KEY'] = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' # --> password
#api = Api(app, version='1.0', title='Your API', description='API description')


entities_data = {}
# entity_model = api.model('Entity', {
#     'name': fields.String,
#     'age': fields.Integer,
#     'gender': fields.String,
#     'address': fields.Nested(api.model('Address', {
#         'country': fields.String,
#         'state': fields.String,
#         'city': fields.String,
#         'street': fields.String,
#         'plz': fields.String,
#     }))
# })

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


@app.route("/user")
class Entities(Resource):
	
	@app.route("/user/getUserByName")
	def get(self):

		# Retrieve entities from the database and return them
		entities = Schuler.query.all()
		return [{"name": entity.name, "course_id": entity.course_id} for entity in entities]


		# if entity_id is None:
		# 	return entities_data
		# else:
		# 	if entity_id in entities_data:
		# 		return {entity_id: entities_data[entity_id]}
		# 	else:
		# 		return {'error': f'Entity with ID {entity_id} not found'}, 404


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
api_url = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
	swagger_url,
	api_url,
	config={
		'app_name': "Your API's Name"
	},
)
app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)




if __name__ == '__main__':
	app.run(debug=True)
	

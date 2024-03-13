from flask import Flask, request, make_response, jsonify, session, redirect, url_for, render_template, current_app
from flask_bcrypt import Bcrypt
from flask_restx import Resource, Namespace, Api, reqparse, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, and_
from flask_restful import marshal
from functools import wraps

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, verify_jwt_in_request, \
    get_jwt
from datetime import datetime, timedelta
from werkzeug.exceptions import BadRequestKeyError
import hashlib
import requests
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import secrets
from sqlalchemy.orm import Session

######################################################  odoo  ##########################################################


app = Flask(__name__, template_folder="templates")
jwt = JWTManager(app)
login_manager = LoginManager(app)

api = Api(app, version='1.0.0', title='My odoo API', description='API checking datat from odoo', doc='/home')

db = SQLAlchemy()

bcrypt = Bcrypt(app)

ns = api.namespace("MyApi", description="sql and odoo")

api.add_namespace(ns)

login_manager.login_view = 'login'  # 'login' should be the endpoint for your login page

###################################### hash pass for secur pass ####################################
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


user_password = "password"
hashed_password = hash_password(user_password)
# print(hashed_password)

app.config[
    'SECRET_KEY'] = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # Add this line to set the secret key
app.config['JWT_SECRET_KEY'] = '447fce4bbc4b8f6da86714945d33fe0590d55e8d90fd1d526a68c774ea9f2d70'  # jwt secrete key


#################################################### Normal Database ############################################
#################################################### Normal Database ############################################
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/feraidon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


#################################################### Normal Database ############################################
#################################################### Normal Database ############################################


############################################ models ##############################################################
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # schulers = db.relationship("Schuler", back_populates="course")


######### create schema on swager page buttom of the form ################
course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String
})


@ns.route("/course")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self):
        return Course.query.all()


########################################################################################################################
########################################################################################################################
# schuler table
class Schuler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    # course = db.relationship("Course", back_populates="schulers")


############ create schema on swager page buttom of the form ##############
schuler_model = api.model("Schuler", {
    "id": fields.Integer,
    "name": fields.String,
    # "schuler":fields.Nested(course_model),
})


@ns.route("/schuler")
class SchulerAPI(Resource):
    @ns.expect("/schuler")
    @ns.marshal_with(schuler_model)
    def get(self):
        return Schuler.query.all()


########################################################################################################################
########################################################################################################################


class Users(UserMixin, db.Model):
    __tablename__ = 'Users'

    mitarbeiter_id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String(50))
    nachname = db.Column(db.String(50))
    position = db.Column(db.String(50))
    abteilung = db.Column(db.String(50))
    gehalt = db.Column(db.DECIMAL(10, 2))
    erfahrungsjahr = db.Column(db.Integer)
    programmiersprache = db.Column(db.String(50))
    zertifikat = db.Column(db.String(50))
    projektnummer = db.Column(db.Integer)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        # print("Hashed Password:", hashed_password)
        self.password = hashed_password

    def check_password(self, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return bcrypt.check_password_hash(hashed_password, self.password)

    def is_active(self):
        # Define your logic for determining if the user is active
        # For example, you could return True if the user has confirmed their email
        return True

    @staticmethod
    def get(user_id, session=None):
        session = session or db.session
        # Replace this with your actual database query
        return session.query(Users).filter_by(mitarbeiter_id=int(user_id)).first()

    def get_id(self):
        return str(self.mitarbeiter_id)


# def get_user_api():
#
#     with app.app_context():
#         db.create_all()
#
#         # Example during user creation
#         new_user = Users(username='feri', password='password')
#         new_user.set_password('password')
#         db.session.add(new_user)
#         db.session.commit()
#
#         # Example during login validation
#         user = Users.query.filter_by(username='feri').first()
#         if user and user.check_password('password'):
#             print("welcome ")
#         return user

# users table
############# create schema on swager page buttom of the form ###########
users_model1 = api.model("Users", {
    "mitarbeiter_id": fields.Integer,
    "vorname": fields.String,
    "nachname": fields.String,
    "position": fields.String,
    "abteilung": fields.String,
    "gehalt": fields.Float,
    "erfahrungsjahr": fields.String,
    "programmiersprache": fields.String,
    "zertifikat": fields.String,
    "projektnummer": fields.Integer,
    "schuler": fields.List(fields.Nested(course_model))
})


@login_required
@ns.route("/users")
class UserAPI(Resource):
    @marshal_with(users_model1)  # without filter input
    def get(self):
        return Users.query.all()


########################################################################################################################
########################################################################################################################

# @app.route("/dashboard")
# @login_required
# def dashboard():
#     with ((app.app_context())):
#         # Example during API call
#         api_response = UserAPI().get()
#         print(api_response)
#         return jsonify(api_response)

@app.route("/dashboard")
@login_required
def dashboard():
    # with app.app_context():
    # Example during API call

    return render_template("swagger.html")


##################################### ###  nested table data with other talbes  ########################################
# from flask_restx import marshal_with
class Dozent(db.Model):
    dozent_id = db.Column(db.Integer, primary_key=True)
    dozent_name = db.Column(db.String(50), unique=True)
    dozent_nachname = db.Column(db.String(100), unique=True)
    dozent_fach = db.Column(db.String(100), unique=True)
    dozent_course = db.Column(db.String(100), unique=True)


dozent_model = api.model("Dozent", {
    "dozent_id": fields.Integer,
    "dozent_name": fields.String,
    "dozent_nachname": fields.String,
    "dozent_fach": fields.String,
    "dozent_course": fields.String,
})

dozent_input_model = api.model("Dozent", {
    "dozent_name": fields.String
})

# felder die zum update sind benötigen requestparse
parser = reqparse.RequestParser()
parser.add_argument('field_to_update', type=str, help='The field to update')


@ns.route("/dozenttest", endpoint='custom_dozent2')  #### ns api
class DozentAPI(Resource):

    @ns.marshal_with(schuler_model)
    def get(self):
        return Schuler.query.all()

    def get(self):
        try:
            # Implement your logic to fetch and return Dozent data
            return {"message": "Dozent data here"}

        except Exception as e:
            return {"error": str(e)}, 500


########################################################################################################################


##################################### authenticatoin ###################################################################


@login_manager.user_loader
def load_user(user_id):
    # Load user from the database by user_id
    # return Users.query.get(int(user_id))
    return Users.query.filter_by(mitarbeiter_id=int(user_id)).first()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Look up the user from the database based on the provided username
        user = Users.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            # Assuming authentication is successful, create a JWT token
            access_token = create_access_token(identity=username)
            # return jsonify(access_token=access_token, message="Login successful")
            return redirect(url_for("home"))

    return render_template('login.html')


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # print(request.headers)
    # verify_jwt_in_request()
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Route to generate a dummy token (for testing purposes)
@app.route("/token", methods=["GET"])
def generate_token():
    user = Users(mitarbeiter_id=1234)
    access_token = create_access_token(identity=user.mitarbeiter_id)
    return jsonify(access_token=access_token, message="Token generated successfully")


# ####################################################### login here ########################################


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_required
# @jwt_required()
@app.route('/docs')
@login_required
def docs():
    return render_template('login.html')


##########################################  test authorization header ##################################################
# @jwt_required()
@login_required
@ns.route("/dozent1", endpoint='custom_dozent1')  ### ns api
class DozentAPI1(Resource):

    @ns.expect(dozent_input_model)
    @ns.marshal_with(dozent_model)
    def post(self):
        data = ns.payload
        new_dozent = Dozent(**data)
        db.session.add(new_dozent)
        db.session.commit()
        return new_dozent

    @ns.expect(dozent_input_model)
    def delete(self):
        data = ns.payload
        dozent_to_delete = Dozent.query.filter_by(id=data['id']).first()
        if dozent_to_delete:
            db.session.delete(dozent_to_delete)
            db.session.commit()
        return dozent_to_delete

    ##################################################################################################################
    @ns.expect(dozent_input_model)
    def put(self):
        data = ns.payload
        dozent_id = data.get('id')  # Use get() to avoid KeyError if 'id' is not present
        if dozent_id is None:
            return {'message': 'Missing or invalid "id" in the request payload'}, 400

        dozent_to_update = Dozent.query.filter_by(id=dozent_id).first()
        if dozent_to_update:
            dozent_to_update.update(data)
            db.session.commit()
            return dozent_to_update
        else:
            return {'message': f'Dozent with id {dozent_id} not found'}, 404

    ##################################################################################################################

    # @ns.doc(description="mit mask feld wird")
    @ns.doc(description="allow functions or not allow functions")
    def options(self):
        return {'allow': 'GET, POST, PUT, DELETE'}, 200, {'Allow': 'GET, POST, PUT, DELETE'}

    ##################################################################################################################
    # patch method für update or aktualisierung
    @ns.expect(dozent_input_model)
    @ns.marshal_with(dozent_model)
    def patch(self):
        args = parser.parse_args()
        dozent_id = args.get('dozent_id')

        if dozent_id is None:
            return {'message': 'Missing or invalid "dozent_id" in the request payload'}, 400

        dozent_to_update = Dozent.query.get(dozent_id)
        if dozent_to_update:
            for key, value in args.items():
                # Update only the specified fields
                setattr(dozent_to_update, key, value)

            db.session.commit()
            return dozent_to_update
        else:
            return {'message': f'Dozent with id {dozent_id} not found'}, 404


# Customizing Swagger UI  background  ########       ##########        ############           ############
# @jwt_required()
# @app.route('/swagger-ui', endpoint='custom_swagger_ui2')
@api.documentation
def custom_swagger_ui():
    """
    Custom Swagger UI configuration.
    """
    return {
        'swagger-ui': True,
        'swagger-url': '/swagger.json',
        'swagger-ui-bundle-js': '/static/swagger-ui-bundle.js',
        'swagger-ui-css': '/static/swagger-ui.css',
        'custom-swagger-css': '/static/custom-swagger.css',
        'swagger-ui-init-js': '/static/swagger-initializer.js',

    }


###########         ##########     Customizing Swagger UI     ############           ############


def token_required():
    user = {
        "id": 1234,
        "name": "feri",
        "nachname": "moh"
    }

    with app.app_context():
        # new_secret_key = secrets.token_hex(32)
        access_token = create_access_token(identity=user)
        response_data = {
            "access_token": access_token,
            "message": "login successful"
        }
        # print(response_data)
        return response_data


# @jwt_required()
@app.route("/swagger-ui")
@login_required
def home():
    return render_template("swagger.html")


# Use the Flask test client to simulate an HTTP request
with app.test_client() as client:
    access_token = token_required()["access_token"]
    # Call your protected route with the test client
    response = client.get('/protected', headers={'Authorization': f'Bearer {access_token}'})
    # print(response.status_code)
    # print(response.get_json())

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="127.0.0.1", port="5000", debug=False)

from flask import Flask, request, make_response, jsonify, session, redirect, url_for, render_template
from flask_restx import Resource, Namespace, Api, reqparse, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, and_
from flask_restful import marshal
from functools import wraps
import jwt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime, timedelta
from werkzeug.exceptions import BadRequestKeyError
######################################################  odoo  ##########################################################

import xmlrpc.client

app = Flask(__name__)
api = Api()
db = SQLAlchemy()
# ai = api.namespace("My Api", description="Login and register")
ns = api.namespace("My Api", description="sql and odoo")
api.init_app(app)
api.add_namespace(ns)

users = {"username": "password"}

#################################################### odoo ##############################################################


url = "http://10.50.200.81:8069"
database = "iad"
user = "xmlrpc"
pwd = "xmlrpc"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# print("Version Details: ", common.version())

uid = common.authenticate(database, user, pwd, {})
# print(uid)
odoo_db_info = {
    'host': 'http://10.50.200.81',
    'port': "8069",
    'database': 'iad',
    'username': 'xmlrpc',
    'password': 'xmlrpc',
}

########################################################################################################################
# create a hash password for secret key
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Example usage
user_password = "password"
hashed_password = hash_password(user_password)

users = []
jwt_password = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMjQ3MjAyOSwianRpIjoiNjViZGRlYzUtYTBjMC00ZmU2LWIyMTAtNDdlM2EzYjkzM2FjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZlcmkiLCJuYmYiOjE3MDI0NzIwMjksImV4cCI6MTcwMjQ3MjkyOX0.ldGfNbCWqEwx7gf9kxgQTedwocukbQ9dthqHjLs_KFI"
app.config[
    "SECRET_KEY"] = hashed_password  # "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" # result von password
app.config["JWT_SECRET_KEY"] = jwt_password
jwt = JWTManager(app)





#################################################### Normal Database ############################################
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/feraidon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


#################################################### Normal Database ############################################


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    # schulers = db.relationship("Schuler", back_populates="course")


class Schuler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    # course = db.relationship("Course", back_populates="schulers")


class Users(db.Model):
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

    def __repr__(self):
        return f"<Users(mitarbeiter_id={self.mitarbeiter_id}, Vorname={self.Vorname}, Nachname={self.Nachname})>"


################################## create schema on swager page buttom of the form #####################################


course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String
})


@ns.route("/course/ data from database mysql")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self):
        return Course.query.all()


########################################################################################################################
################################## create schema on swager page buttom of the form #####################################
schuler_model = api.model("Schuler", {
    "id": fields.Integer,
    "name": fields.String,
    # "schuler":fields.Nested(course_model),
})


@ns.route("/schuler from database mysql")
class SchulerAPI(Resource):
    @ns.expect("/schuler")
    @ns.marshal_with(schuler_model)
    def get(self):
        return Schuler.query.all()


########################################################################################################################
################################## create schema on swager page buttom of the form #####################################
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


@ns.route("/users from database mysql")
class UserAPI(Resource):

    @marshal_with(users_model1)  # without filter input
    def get(self):
        return Users.query.all()


########################################################################################################################
########################################################################################################################


##################################### ###  nested table data with other talbes  ########################################
# from flask_restx import marshal_with
class Dozent(db.Model):
    dozent_id = db.Column(db.Integer, primary_key=True)
    dozent_name = db.Column(db.String(50), unique=True)
    dozent_nachname = db.Column(db.String(100), unique=True)
    dozent_fach = db.Column(db.String(100), unique=True)
    dozent_course = db.Column(db.String(100), unique=True)

    # # Define the relationship properly
    # Dozent.schulers = db.relationship("Dozent", back_populates="schuler", remote_side=Dozent.dozent_id)
    # Dozent.schuler = db.relationship("Dozent", back_populates="schulers")


dozent_model = api.model("Dozent", {
    "dozent_id": fields.Integer,
    "dozent_name": fields.String,
    "dozent_nachname": fields.String,
    "dozent_fach": fields.String,
    "dozent_course": fields.String,

    # "schuler":fields.Nested(schuler_model),
    # "name":fields.List(fields.Nested(schuler_model))
})

dozent_input_model = api.model("Dozent", {
    # "dozent_id":fields.Integer,
    "dozent_name": fields.String,
    # "dozent_nachname":fields.String,
    # "dozent_fach":fields.String,
    # "dozent_course":fields.String,
})

# felder die zum update sind benötigen requestparse
parser = reqparse.RequestParser()
parser.add_argument('field_to_update', type=str, help='The field to update')


# authentication need this
def valid_login(username, password):
    # Add your authentication logic here (e.g., check username and password against a database)
    return username == "feri" and password == "password"



# @api.route("/dozent")
class DozentAPI(Resource):



    @jwt_required()  # This decorator ensures that a valid JWT is present in the request
    def get(self):
        try:
            # Implement your logic to fetch and return Dozent data
            return {"message": "Dozent data"}

        except Exception as e:
            return {"error": str(e)}, 500


# Add the resource to the API
api.add_resource(DozentAPI, '/')


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Render the login form when accessing the root URL
        return render_template("login.html")
    elif request.method == "POST":
        # Process login form submission when the form is submitted
        username = request.form["username"]
        password = request.form["password"]

        if valid_login(username, password):
            # If login is successful, create a JWT token
            token = create_access_token(identity=username)
            return jsonify({"token": token})

        return make_response("Unable to verify", 403, {"WWW-Authenticate": "Basic realm='Authentication Failed!'"})




####################################################   ns dozent buttons ##################################
####################################################   ns dozent buttons ##################################

# @api.route("/dozent")
class DozentAP2(Resource):

    # @api.doc(params={'X-Fields': {'description': 'An optional fields mask', 'type': 'string', 'format': '$mask', 'in': 'header'}})
    # @api.payload("/dozent")
    # @ns.doc(model=dozent_model)

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

    @app.route("/dozent", methods=["GET", "POST"])
    def auth(self):
        if request.method == "GET":
            current_user = get_jwt_identity()
            return f"JWT is verified for user: {current_user}. Welcome to my page."
        elif request.method == "POST":
            # Your POST logic here
            access_token = create_access_token(identity='example_user')
            return {'access_token': access_token}



if __name__ == "__main__":
    app.run(debug=True)
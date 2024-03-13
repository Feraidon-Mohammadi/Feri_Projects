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
#print(hashed_password)

app.config[
    'SECRET_KEY'] = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # Add this line to set the secret key
app.config['JWT_SECRET_KEY'] = '447fce4bbc4b8f6da86714945d33fe0590d55e8d90fd1d526a68c774ea9f2d70'  # jwt secrete key


################################################## odoo ################################################################
################################################## odoo ################################################################
import xmlrpc.client

class Get_Odoo_Dta:
    # Odoo database connection information
    odoo_db_info = {
        'host': 'http://xx.xx.xx.xx',
        'port': "xxxx",
        'database': 'xxxx',
        'username': 'xxxxx',
        'password': 'xxxxxx',
    }

    # Connect to the Odoo database using XML-RPC
    url = "http://xx.xx.xx.xx:xxxx"

    ############################################################# fixed ##############################################
    # Odoo XML-RPC server URL
    odoo_url = 'http://{0}:{1}/xmlrpc/2'.format(odoo_db_info['host'], odoo_db_info['port'])

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(odoo_db_info['database'], odoo_db_info['username'], odoo_db_info['password'], {})

    model1 = 'res.partner'
    model2 = 'de_iad_tm.measure'
    model3 = 'de_iad_tm.special_day'

    ######
    # Create an XML-RPC object for the database
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    domain = [[['name', "=", "any"]]]


    partner_ids = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model2, 'search_read',
                                    domain)



    limit = 2

######################################## old data 1 #########################################
    records1 = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'],model1, 'search_read',

                                 partner_ids,{'fields': ['id', 'display_name', "education_end_date", "education_school_day_total", "active_education_plan_id", "education_start_date", 'vorname', 'nachname', 'forename', 'name',"measure_number", "city","street", "phone"], "limit":limit})
    #print(f"old data: {records1}")

################################### new data ################################################
    records2 = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model2, 'search_read',
                                 partner_ids,{'fields': ["education_end_date", "education_school_day_total", "active_education_plan_id", "education_start_date", "measure_name",'Kurzbezeichnung', "measure_number", "number", "special_day_ids", "start_date", "end_date", "location_id", "measure_type", "long_name", 'forename', "name", "tag_ids", "city", 'display_name', "street", "phone"],"limit": 10} )
    #print(f"new data specialdays: {records2}")

############################################## new id #########################################
    records3 = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model3, 'search_read', partner_ids,{'fields': ["id","name","education_end_date", "education_school_day_total", "active_education_plan_id", "education_start_date" ,"Maßnahmenummer", "measure_name","measure_number", 'Kurzbezeichnung',"startdatum","Kurzbezeichnung"],"limit": 2} )
    #print(f"new data specialday ids: {records3}")






#############################Retrieve detailed information for each special_day_id m###################

    # for record in records2:
    #     special_day_details = []
    #     for special_day_id in record['special_day_ids']:
    #         # Make an API request to get detailed information for each special_day_id from the related model
    #         special_day_info = models.execute_kw(
    #             odoo_db_info['database'], uid, odoo_db_info['password'],
    #             'de_iad_tm.special_day', 'read', [special_day_id],
    #             {'fields': ['id', 'startdatum', 'enddatum', 'typ', 'standort', 'maßnahmenummer', 'tag', 'nummer']}
    #         )
    #         special_day_details.append(special_day_info[0])
    #
    #     # Update the 'special_day_ids' field with detailed information
    #     record['special_day_ids'] = special_day_details
    #
    # # Now 'records2' contains detailed information for each special_day_id from the related model
    # print(records2)








################################ need ##################################
    # # Retrieve detailed information for each special_day_id
    # for record in records2:
    #     special_day_details = []
    #     for special_day_id in record['special_day_ids']:
    #         # Make an API request to get detailed information for each special_day_id
    #         special_day_info = models.execute_kw(
    #             odoo_db_info['database'], uid, odoo_db_info['password'],
    #             'de_iad_tm.special_day', 'read', [special_day_id],
    #             {'fields': ['id', 'Startdatum', 'Enddatum', 'Typ', 'Standort', 'Maßnahmenummer', 'Tag', 'Nummer',"Tags",]}
    #         )
    #         special_day_details.append(special_day_info[0])
    #
    #     # Update the 'special_day_ids' field with detailed information
    #     record['special_day_ids'] = special_day_details
    #
    #     # Now 'records1' contains detailed information for each special_day_id
    #     print(records2)


######################## oldest ############################
# #Define a model for the Odoo data #new way for special_day
odoo_model = api.model("measur_data", {
    "id": fields.Integer,
    "name": fields.String,
    "phone": fields.String,
    "tag_ids": fields.List(fields.Integer),
    'location_id': fields.List(fields.String),
    "special_day_ids": fields.List(fields.Integer),
    
    'special_day_ids1': fields.List(fields.Nested(api.model('special_data', {
        'id': fields.Integer,
        'start_date': fields.String,
        'end_date': fields.String,
        'type': fields.String,
        'location': fields.String,
        # Add other fields from the related model as needed
    }))),
})

################################## new-fixed 2024 #####################################
# # Define a model for the Odoo data #new way for special_day
# odoo_model = api.model("get_odoo_data", {
#     "id": fields.Integer,
#     "name": fields.String,


#     "special_day_ids": fields.List(fields.Nested
#         (api.model
#             ('special_day_data',
#                 {'id': fields.Integer,
#                 "display_name": fields.String,
#                 "forename": fields.String,
#                 "phone": fields.String,
#                 }
#             )
#         )
#     )
# })




################################################### odoo  fixed and worked ###################################################


################################### measure model fixed ########################
@ns.route('/odoo_data2/')
class OdooDataResource(Resource):

    @ns.doc(description="mit mask feld wird filterierte daten angezeigt, und mit comma nach jede value für meherere")
    @ns.marshal_list_with(odoo_model)
    def get(self):  # Add 'self' as the first parameter
        x = Get_Odoo_Dta.records2

        # Assuming get_odoo_data returns a list of dictionaries
        if not x:
            return {"message": "Data not found"}, 404
        return x



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
        #print("Hashed Password:", hashed_password)
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
        #print(response_data)
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
    #print(response.status_code)
    #print(response.get_json())

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="127.0.0.1", port="5000", debug=False)

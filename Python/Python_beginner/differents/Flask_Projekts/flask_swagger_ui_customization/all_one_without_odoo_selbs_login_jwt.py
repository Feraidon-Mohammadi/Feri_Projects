from flask import Flask, request, make_response, jsonify, session, redirect, url_for, render_template
from flask_restx import Resource, Namespace, Api, reqparse, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, and_
from flask_restful import marshal
from functools import wraps

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime, timedelta
from werkzeug.exceptions import BadRequestKeyError
import hashlib



from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user
from flask_bcrypt import Bcrypt

from flask_httpauth import HTTPBasicAuth
######################################################  odoo  ##########################################################

app = Flask(__name__, template_folder="templates")
api = Api(app, version='1.0.0', title='My odoo API', description='API checking datat from odoo', doc='/home' ,authorizations={
              'apiKey': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization'
              },
              'basicAuth': {
                  'type': 'basic'
              }
          },
          security=['apiKey', 'basicAuth']
          )

auth = HTTPBasicAuth()
db = SQLAlchemy()
bcrypt = Bcrypt(app)
ns = api.namespace("MyApi", description="sql and odoo")
# api.init_app(app)
api.add_namespace(ns)



# Mocked user data (replace this with your actual authentication logic)
users = {
    'username': 'password',
}


login_manager = LoginManager(app)
login_manager.login_view = 'login'  # 'login' should be the endpoint for your login page
login_manager.init_app(app)
# users = {"username": "password"}

jwt = JWTManager(app)

###################################### hash pass for secur pass ####################################
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
user_password = "password"
hashed_password = hash_password(user_password)






#################################################### Normal Database ############################################
#################################################### Normal Database ############################################
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/mysql_server_name"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = hashed_password  # Add this line to set the secret key
db.init_app(app)
#################################################### Normal Database ############################################
#################################################### Normal Database ############################################


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # schulers = db.relationship("Schuler", back_populates="course")


######### create schema on swager page buttom of the form ################
course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String
})


@auth.verify_password
def verify_password(username, password):
    # Your authentication logic here
    return username == 'username' and password == 'password'



@ns.route("/course")
class CourseAPI(Resource):
    @ns.marshal_list_with(course_model)
    @ns.doc(description="just authenticated users have access to this data",security='basicAuth')
    @auth.login_required
    def get(self):
        return Course.query.all()



# Authentication callback
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        g.current_user = username
        return True
    return False

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

    # unlucked icon on get method
    @ns.doc(description="just just user with with login have access  to this data ",security=[{'Bearer Auth': 'Write access'}])  # This line adds the "Authentication" button
    @ns.marshal_list_with(schuler_model)
    def get(self):
        # Your logic here
        return Schuler.query.all()


########################################################################################################################
########################################################################################################################



class Users(db.Model, UserMixin):
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
        print("Hashed Password:", hashed_password)
        self.password = hashed_password

    def check_password(self, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return bcrypt.check_password_hash(hashed_password, self.password)

    def get_id(self):
        return str(self.mitarbeiter_id)

def get_user_api():

    with app.app_context():
        db.create_all()

        # Example during user creation
        new_user = Users(username='feri', password='password')
        new_user.set_password('password')
        db.session.add(new_user)
        db.session.commit()

        # Example during login validation
        user = Users.query.filter_by(username='feri').first()
        if user and user.check_password('password'):
            print("welcome ")
        return user

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

@ns.route("/users")
class UserAPI(Resource):
    @marshal_with(users_model1)  # without filter input
    @ns.doc(description="just authenticated users have access to this data ",security=[{'Bearer Auth': 'Write access'}])
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


@ns.route("/dozent", endpoint='custom_dozent2')  #### ns api
class DozentAPI(Resource):


    @jwt_required()
    def get(self):
        try:
            # Implement your logic to fetch and return Dozent data
            return {"message": "Dozent data"}

        except Exception as e:
            return {"error": str(e)}, 500


########################################################################################################################



##################################### authenticatoin ###################################################################



@login_manager.user_loader
def load_user(user_id):
    # Load user from the database by user_id
    return Users.query.get(int(user_id))



def authenticate_user(username, password):
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = authenticate_user(username, password)
        if user:
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return make_response("Unable to verify", 403, {"WWW-Authenticate": "Basic realm='Authentication Failed!'"})



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Protected route using Flask-Login
@app.route('/protected', methods=['GET'])
def protected():

    # return f"Logged in as: {current_user.username}"
    # return jsonify(logged_in_as=current_user), 200
    return redirect(url_for("home"))





@login_required
@app.route("/dashboard")
def dashboard():
    with app.app_context():
        # Example during API call
        api_response = UserAPI().get()
        print(api_response)
        return jsonify(api_response)


##########################################  test authorization header ##################################################

@ns.route("/dozent", endpoint='custom_dozent1')  ### ns api
class DozentAP(Resource):


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


@app.route("/swagger-ui")
@login_required
def home():
    return  render_template("swagger.html")



if __name__ == "__main__":
    app.run(debug=True)
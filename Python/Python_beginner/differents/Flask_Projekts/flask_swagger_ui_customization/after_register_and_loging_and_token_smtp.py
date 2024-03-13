import datetime
import hashlib
import smtplib
from datetime import timedelta, datetime

import requests
from flask import Flask, request, jsonify, render_template, request, redirect, url_for,make_response
from flask_migrate import Migrate
from flask_restx import Resource, Namespace, Api,fields
from flask_sqlalchemy import SQLAlchemy
from flask_restful import marshal
from flask_httpauth import HTTPBasicAuth
import jwt
import bcrypt

# smtp need
import secrets
import smtplib
import ssl

# to create table in mysql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Boolean, DateTime

# to add email parts
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# to remove unconfirmed data
from apscheduler.schedulers.background import BackgroundScheduler


def create_app():
    app = Flask(__name__, template_folder="templates")
    api = Api(app, version='1.0.0', title='My odoo API', description='API checking datat from odoo', doc='/home',
              authorizations={
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
    db = SQLAlchemy()
    ns = Namespace("MyApi", description="sql and odoo")
    auth = HTTPBasicAuth()
    api.add_namespace(ns)





########################################################################################################################
    # mysql
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/name_of_mysql_server"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)



    ############# to initialize data in database mysql should use this to migrate the data
    migrate = Migrate(app, db)
    # Create tables inside Flask application context
    with app.app_context():
        # Run migrations
        db.create_all()
        migrate.init_app(app, db)
    ############################### end migration data ###################################




    return auth, app, api, db, ns


########################################################################################################################




auth, app, api, db, ns = create_app()




################################################## odoo ################################################################
################################################## odoo ################################################################
import xmlrpc.client



class Get_Odoo_Data:
    # Odoo database connection information
    odoo_db_info = {
        'host': 'http://xx.xx.xx.xx',
        'port': "xxxx",
        'database': 'xxxx',
        'username': 'xxxxxx',
        'password': 'xxxxxxxx',
    }

    # Connect to the Odoo database using XML-RPC
    url = "http://xx.xx.xx.xx:xxxx"

    ############################################################# fixed ##############################################
    # Odoo XML-RPC server URL
    odoo_url = 'http://{0}:{1}/xmlrpc/2'.format(odoo_db_info['host'], odoo_db_info['port'])

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(odoo_db_info['database'], odoo_db_info['username'], odoo_db_info['password'], {})

    model1 = 'xxx.xxxxxx'
    model2 = 'xxxxx.xxxxxxxxx'
    model3 = 'xxxxxxxxxx.xxxxxxxxxxx'

    ######
    # Create an XML-RPC object for the database
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    domain = [[['name', "=", "any"]]]

    partner_ids = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model2, 'search_read',
                                    domain)

    limit = 10

    ######################################## old data 1 #########################################
    records1 = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model1, 'search_read',

                                 partner_ids, {'fields': ['id', 'display_name', "education_end_date",
                                                          "education_school_day_total", "active_education_plan_id",
                                                          "education_start_date", 'vorname', 'nachname', 'forename',
                                                          'name', "measure_number", "city", "street", "phone"],"limit":limit})
    # print(f"old data: {records1}")

    ################################### new data ################################################
    records2 = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model2, 'search_read',
                                 partner_ids, {'fields': ["education_end_date", "education_school_day_total",
                                                          "active_education_plan_id", "education_start_date",
                                                          "measure_name", "phone"]})
    # print(f"new data specialdays: {records2}")

    ############################################## new id #########################################
    records3 = models.execute_kw(odoo_db_info['database'], uid, odoo_db_info['password'], model3, 'search_read',
                                 partner_ids, {
                                     'fields': ["id", "name","measure_name", "education_end_date", "education_school_day_total",
                                                "active_education_plan_id", "education_start_date", "Maßnahmenummer",
                                                "measure_name", "measure_number", 'Kurzbezeichnung', "startdatum",
                                                "Kurzbezeichnung"], "limit": 2})
    # print(f"new data specialday ids: {records3}")



######################## oldest ############################
# #Define a model for the Odoo data #new way for special_day
odoo_model = api.model("measur_data", {
    "id": fields.Integer,
    "name": fields.String,
    "measure_name":fields.String,
    "long_name": fields.String,
    'start_date': fields.String,
    'end_date': fields.String,
    'measure_type': fields.String,
    "number": fields.String,
    "display_name": fields.String,

    "forename": fields.String,
    "city": fields.String,
    "street": fields.String,
    "phone": fields.String,

    "tag_ids": fields.List(fields.Integer),
    'location_id': fields.List(fields.String),
    "special_day_ids": fields.List(fields.String),

})


################################### measure model fixed ########################
@ns.route('/odoo All data /')
class OdooDataResource(Resource):

    @ns.doc(description="just authenticated users have access to this data", security='basicAuth')
    #@ns.doc(description="mit mask feld wird filterierte daten angezeigt, und mit comma nach jede value für meherere")
    @ns.marshal_list_with(odoo_model)
    def get(self):  # Add 'self' as the first parameter

        records1 = Get_Odoo_Data.records1
        records2 = Get_Odoo_Data.records2
        records3 = Get_Odoo_Data.records3

        #all_of_them = records1 + records2 + records3

        # Assuming 'records' is a list of dictionaries
        if not records1:
            return {"message": "Data not found"}, 404

        return records1


######################################### res_partner model  model1 fixed #########################



########## +++++ it working perfect and find from every model when data are not exist in a model +++++ ########
@ns.route('/odoo data1/<string:measure_name>/<string:number>/<int:id>')
class OdooDataResource(Resource):

    # old data
    @ns.doc(description="just authenticated users have access to this data", security='basicAuth')
    #@ns.doc(description="mit mask feld wird filterierte daten angezeigt, und mit comma nach jede value für meherere")
    @ns.marshal_list_with(odoo_model)
    def get(self, measure_name, number, id):
        # Fetch Odoo data
        x1 = Get_Odoo_Data.records1
        x2 = Get_Odoo_Data.records2
        x3 = Get_Odoo_Data.records3


        filtered_data1 = [item for item in x1 if
                         item.get('measure_name') == measure_name or item.get('number') == number
                         or item.get("id") == id]

        filtered_data2 = [item for item in x2 if
                         item.get('measure_name') == measure_name or item.get('number') == number
                         or item.get("id") == id]

        filtered_data3 = [item for item in x3 if
                         item.get('measure_name') == measure_name or item.get('number') == number
                         or item.get("id") == id]

        # Assuming get_odoo_data returns a list of dictionaries
        if not filtered_data1 and not filtered_data2 and not filtered_data3:
            return {"message": "Data not found"}, 404
        return filtered_data1 + filtered_data2 + filtered_data3







@ns.route("/odoo mit zwei model combiniert/<string:name>/<string:number>/<int:id>")
class Odoo_third(Resource):

    @ns.doc(description="just authenticated users have access to this data", security='basicAuth')
    @ns.marshal_list_with(odoo_model)
    def get(self, name, number, id):
        first_record = Get_Odoo_Data.records1
        second_record = Get_Odoo_Data.records2

        if not first_record and not second_record:
            return {"message": "Data not Found"}, 404

        # Combine the data from both models
        combined_data = []

        # Filter records based on provided parameters
        first_records = [item for item in first_record if
                         item.get('name') == name or item.get('number') == number or item.get("id") == id]

        second_records = [item for item in second_record if
                          item.get('name') == name or item.get('number') == number or item.get("id") == id]

        for record1 in first_records:
            # Create a new dictionary for each item
            combined_item = {}

            # Merge data from the first model
            combined_item.update({
                "forename": record1.get("forename"),
                "city": record1.get("city"),
                "street": record1.get("street"),
                "phone": record1.get("phone"),
            })

            # Find the corresponding record in the second model
            record2 = next((r for r in second_records if r["id"] != id), {})
            # record2 = next((r for r in second_records if r["id"] == id), {})
            # record2 = next((r for r in second_records if r["id"] == id), None)
            if record2 is None:
                return {"message": "Second model data not found for the given id"}, 404

            # Merge data from the second model
            combined_item.update(record2)

            # Append the combined item to the result list
            combined_data.append(combined_item)

        if not combined_data:
            return {"message": "Data not Found"}, 404

        return combined_data










######################################## find by id ######################################
## old data
# @ns.doc(description="mit mask feld wird filterierte daten angezeigt, und mit comma nach jede value für meherere")
# @ns.marshal_list_with(odoo_model)
# def get(self, id):
#     # Fetch Odoo data
#     x = Get_Odoo_Dta.records1
#     filtered_data = [item for item in x if item.get("id") == id]
#
#     # Assuming get_odoo_data returns a list of dictionaries
#     if not filtered_data:
#         return {"message": "Data not found"}, 404
#     return filtered_data


########################################## new for all data ###########################

@ns.doc(description="mit mask feld wird filterierte daten angezeigt, und mit comma nach jede value für meherere")
@ns.marshal_list_with(odoo_model)
def get(self):
    # Fetch Odoo data
    x = Get_Odoo_Data.records2

    # Assuming get_odoo_data returns a list of dictionaries
    if not x :
        return {"message": "Data not found"}, 404
    return x










##############################+++++++++++++++++++++++++++++#################################
# create table in database


# Define the table structure
metadata = MetaData()
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(80), unique=True, nullable=False),
    Column('email', String(120), unique=True, nullable=False),
    Column('password', String(200), nullable=False),
    Column('vorname', String(80), nullable=False),
    Column('nachname', String(80), nullable=False),
    Column('salt', String(120), nullable=False),
    Column('confirmation_token', String(255), unique=True, nullable=True),
    Column('expiration_time', DateTime, nullable=True),
    Column('confirmed', Boolean, nullable=True, default=False),

)

# MySQL database URI
x ="mysql://root:password@localhost/feraidon"
engine = create_engine(x)

# Create the table in the database
metadata.create_all(engine)

##############################+++++++++++++++++++++++++++++#################################






# secure key
SECRET_KEY = 'Rainbow_Secret'




# url = 'http://127.0.0.1:5000/home'
# headers = {'Authorization': 'Bearer YOUR_JWT_TOKEN'}
# response = requests.post(url, headers=headers)
#
#
# print(response.status_code)
# print(response.json())







# add data in database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    vorname = db.Column(db.String(80), nullable=False)
    nachname = db.Column(db.String(80), nullable=False)
    salt = db.Column(db.String(120), nullable=False)
    confirmation_token = db.Column(db.String(255), unique=True, nullable=True)
    expiration_time = db.Column(db.DateTime, nullable=True)
    confirmed = db.Column(db.Boolean, default=False)


def delete_expired_unconfirmed_users():
    with app.app_context():
        expiration_time_threshold = datetime.utcnow() - timedelta(hours=1)
        expired_users = Users.query.filter_by(confirmed=False).filter(Users.expiration_time < expiration_time_threshold).all()

        for user in expired_users:
            db.session.delete(user)

        db.session.commit()

# Initialize the scheduler
scheduler = BackgroundScheduler()

# Schedule the cleanup function to run every 1 hours
scheduler.add_job(delete_expired_unconfirmed_users, 'interval', hours=1)

# Start the scheduler
scheduler.start()




def generate_confirmation_token(expiration_hours=1):

    # Calculate expiration timestamp (current time + expiration duration)
    expiration_time = datetime.utcnow() + timedelta(hours=expiration_hours)

    # Generate a token
    confirmation_token = secrets.token_urlsafe(30)
    return confirmation_token, expiration_time



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirmpassword  = request.form.get("confirmpassword")
            vorname = request.form.get('vorname')
            nachname = request.form.get('nachname')

            # Check if passwords match
            if password != confirmpassword:
                warning_message = "Password and confirm password do not match."
                return render_template('register.html', warning_message=warning_message)


            salt = secrets.token_hex(16)  # 32 characters
            print(salt)
            hashedpwd = hashlib.sha3_256((password + salt).encode()).hexdigest()

            # Generate confirmation token for more security
            confirmation_token, expiration_time = generate_confirmation_token()


            # Save the data to the database
            new_user = Users(username=username, email=email, password=hashedpwd, salt=salt, vorname=vorname, nachname=nachname, confirmation_token=confirmation_token, expiration_time=expiration_time, confirmed=False )





            # Send confirmation email
            send_confirmation_email(email, confirmation_token,expiration_time )

            # if confirmed email than commit data
            db.session.add(new_user)
            db.session.commit()



            # Check if the token is expired
            if is_confirmation_token_expired(expiration_time):
                print("Token is expired")
            else:
                print("Token is still valid")


            return redirect(url_for('registration_success'))
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error during registration: {str(e)}")
            return "Registration failed. Please try again."

    return render_template('register.html')


def send_confirmation_email(email, confirmation_token , expiration_time):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    mail_server = "xxxxxxxxxxxxxx@gmail.com"  # Enter your address
    password = "rxyjkbrltnnjfgearpil"

    confirmation_link = url_for('confirm_email', token=confirmation_token, _external=True)

    # Create a MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = "IAD GmbH <meilserver@gmail.com>"
    msg['To'] = email
    msg['Subject'] = "Confirmation Email"

    # Attach the message body
    body = f"""\
        Hi Dear user,

        Thank you for signing up! To complete your registration, 
        please click on the following link to confirm your email address:

        {confirmation_link}

        If you didn't sign up for our service, please ignore this email.

        Regards,
        iad GmbH
        """
    msg.attach(MIMEText(body, 'plain'))

    # Use the smtplib code to send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(mail_server, password)
        server.sendmail(mail_server, email, msg.as_string())


def is_confirmation_token_expired(expiration_time):
    now = datetime.utcnow()
    return now > expiration_time





@app.route('/confirm_email/<token>', methods=['GET'])
def confirm_email(token):
    user = Users.query.filter_by(confirmation_token=token).first()

    if user and not user.confirmed:
        # Check if the confirmation token is still valid (not expired)
        if not is_confirmation_token_expired(user.expiration_time):
            user.confirmed = True
            db.session.commit()
            return "Email confirmed successfully!"
        else:
            return "Confirmation token has expired."
    else:
        return "Invalid confirmation token."






@app.route('/registration_success', methods=['GET'])
def registration_success():
    return "Registration successful!"







def retrieve_from_database(username):
    # Query the database to retrieve the stored password and salt for the given username
    user = db.session.query(Users).filter_by(username=username).first()
    print(user)

    if user:
        stored_password = user.password # mean hashed_password
        salt = user.salt
        return stored_password, salt
    else:
        return None, None

# User login verification
def verify_user(username, provided_password):
    # Retrieve hashed password and salt from the database
    stored_password, salt = retrieve_from_database(username)

    if stored_password and salt:
        # Combine the provided password with the stored salt
        combined_password = hashlib.sha3_256((provided_password + salt).encode()).hexdigest()

        # Compare the combined password with the stored hashed password directly
        if combined_password == stored_password:
            return True
        else:
            return False
    else:
        return False





# Define your data model
model = api.model('Model', {
    'data': fields.String(required=True, description='Some data'),
})




@app.route('/login', methods=['GET'])
def render_login():
    return render_template('login.html')


# Endpoint to obtain a JWT token
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    provided_password = request.form.get('password')

    user = db.session.query(Users).filter_by(username=username).first()

    if user and user.salt:
        # Hash the provided password with the stored salt
        combined_password = hashlib.sha3_256((provided_password + user.salt).encode()).hexdigest()

        # Compare the combined password with the stored hashed password directly
        if combined_password == user.password:
            # Create access and refresh tokens
            access_token, refresh_token = create_tokens(user.id)

            # Set the tokens in HTTP-only cookies
            response = make_response({'message': 'Login successful'}, 200)
            response.set_cookie('access_token', access_token, httponly=True)
            response.set_cookie('refresh_token', refresh_token, httponly=True)

            return redirect(url_for('Entities_get'))
    return {'message': 'Invalid credentials'}, 401


# Function to create a JWT token with refresh token
def create_tokens(user_id):
    try:
        user = db.session.get(Users, user_id)

        if user:
            # Create access token
            access_token_expiration = datetime.utcnow() + timedelta(hours=1)
            access_payload = {
                'user_id': user.id,
                'vorname': user.vorname,
                'nachname': user.nachname,
                'exp': access_token_expiration,
            }
            access_token = jwt.encode(access_payload, SECRET_KEY, algorithm='HS256')

            # Create refresh token
            refresh_token_expiration = datetime.utcnow() + timedelta(days=30)  # Adjust as needed
            refresh_payload = {
                'user_id': user.id,
                'exp': refresh_token_expiration,
            }
            refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm='HS256')

            return access_token, refresh_token

        else:
            print("User not found")
            return None, None
    except Exception as e:
        print("Error during token creation:", e)
        return None, None


@app.route('/refresh_token', methods=['POST'])
def refresh_token():
    refresh_token = request.cookies.get('refresh_token')

    try:
        refresh_payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])
        user_id = refresh_payload['user_id']

        # Create a new access token
        access_token, _ = create_tokens(user_id)

        # Set the new access token in an HTTP-only cookie
        response = make_response({'message': 'Token refreshed successfully'}, 200)
        response.set_cookie('access_token', access_token, httponly=True)

        return response
    except jwt.ExpiredSignatureError:
        return {'message': 'Refresh token has expired'}, 401
    except jwt.InvalidTokenError:
        return {'message': 'Invalid refresh token'}, 401









# Protected endpoint that requires a valid JWT


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    schulern = db.relationship("Schuler", back_populates="course")


# Create schema on Swagger page bottom of the form
course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String
})


class Schuler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    course = db.relationship("Course", back_populates="schulern")


# Create schema on Swagger page bottom of the form
schuler_model = api.model("Schuler", {
    "id": fields.Integer,
    "name": fields.String,
    # "schuler": fields.Nested(course_model),
})


@ns.route("/course")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self):
        return Course.query.all()


@ns.route("/schuler")
class SchulerAPI(Resource):
    @ns.expect("/schuler")
    @ns.marshal_with(schuler_model)
    def get(self):
        return Schuler.query.all()




users_model = api.model("Users", {
    "id": fields.Integer,
    "username":fields.String,
    "password":fields.String,
    "schuler": fields.List(fields.Nested(course_model))
})



@ns.route('/protected')
class ProtectedResource(Resource):
    @ns.expect(users_model)
    def post(self):
        token = request.headers.get('Authorization')
        if not token:
            return {'message': 'Missing token'}, 401

        try:
            # Decode the token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = decoded_token.get('sub')
            return {'message': f'Protected endpoint accessed by {current_user}'}
        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired'}, 401
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token'}, 401






@ns.route("/home")
class Entities(Resource):

    def get(self):
        # Retrieve entities from the database and return them
        entities = Schuler.query.all()
        return [{"name": entity.name, "course_id": entity.course_id} for entity in entities]

    @ns.expect(course_model)
    def post(self):
        try:
            data = request.json
            new_entity = Schuler(name=data['name'], course_id=data['course_id'])
            db.session.add(new_entity)
            db.session.commit()
            return {"message": "Entity added successfully"}, 201
        except Exception as e:
            return {"message": f"Error: {str(e)}"}, 500





if __name__ == "__main__":
    app.run(debug=True)

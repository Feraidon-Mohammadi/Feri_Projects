import socket
import traceback
from datetime import timedelta
from bcrypt import gensalt, hashpw
from flask import request, g, make_response
from flask_restx import Resource, reqparse
from sqlalchemy import or_, create_engine
from sqlalchemy.orm import Session
from app.models.user_api_models import create_user_models
from app.utils.email_utils import generate_confirmation_token, send_confirmation_email, is_valid_email
from app import require_role
from app.models.user_api_models import UserModel
from apscheduler.schedulers.background import BackgroundScheduler


def setup_api_routes(ns_admin, ns_self_user, ns_help, auth, app, api):
    """
    Create a new partner record in Odoo.

    :param ns_admin: namespace admin für Account management.
    :param ns_self_user: anzeigen und nutzen current user model für aktuele benutzer.
    :param ns_help: for send email to support services.
    :param auth: authentication mechanism used Httpbasicauth
    :param api: instance von Api.
    :param app: application instance.
    :return: json format von daten.
    """

    """ User_Model """
    users_model, current_user_model, help_model = create_user_models(ns_admin, ns_self_user, ns_help)

    database_file = 'iad_database2.db'
    engine = create_engine(f'sqlite:///instance/{database_file}', echo=False)

    # from flask_caching import Cache
    # cache = Cache(app, config={'CACHE_TYPE': 'simple'})
    """ erhöhung geschwindigkeit von get methods mit storing cache """

    @ns_admin.route('/Add_user')
    class SuperUserResource(Resource):

        @auth.login_required
        @ns_admin.expect(users_model)
        @require_role('superuser')
        def post(self, ):
            try:
                # Parse data from the request
                data = api.payload

                # print(f"daten die werden in database gespeichert:---------> {data}")

                # Check if the data matches default values default valuse should not store in database
                if (
                        data['username'] == "string"
                        and data['email'] == "string"
                        or data['password'] == "string"
                        or data['vorname'] == "string"
                        or data['nachname'] == "string"
                        and data['is_super_user'] is False
                ):
                    return {'error': 'Default values are not allowed.'}, 400

                # Create a new superuser only if it's a superuser and has a valid email
                if data['is_super_user']:

                    if not is_valid_email(data['email']):
                        return {'error': 'Invalid email address for super user'}, 400

                    with (Session(engine) as session):
                        # Check if the username or email already exists
                        existing_user = session.query(UserModel).filter(
                            or_(UserModel.vorname == data['vorname'], UserModel.nachname == data['nachname'],
                                UserModel.email == data['email'])).first()

                        if existing_user:
                            # User with the same username or email already exists
                            return {'error': 'Username or email already exists'}, 400

                        # Generate a salt
                        salt = gensalt().decode("utf-8")

                        hashed_password = hashpw(data['password'].encode('utf-8'), salt.encode('utf-8'))

                        # Generate a confirmation token
                        confirmation_token = generate_confirmation_token()

                        # Create a new superuser
                        new_user = UserModel(
                            username=data['username'],
                            email=data['email'],
                            # You can keep it as None for non-super users
                            password=hashed_password.decode("utf-8"),
                            vorname=data['vorname'],
                            nachname=data['nachname'],
                            salt=salt,
                            confirmation_token=confirmation_token,
                            expiration_time=datetime.utcnow() + timedelta(minutes=1),

                            confirmed=False,
                            is_super_user=data['is_super_user']
                        )

                        def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
                            try:
                                socket.create_connection((host, port), timeout=timeout)
                                return True
                            except OSError:
                                return False

                        internet_connection = check_internet_connection()

                        if not internet_connection:
                            return {'connection Error': 'Failed to send email, user not created'}, 500

                        send_confirmation_email(email=data['email'],
                                                confirmation_token=confirmation_token,
                                                expiration_time=datetime.utcnow() + timedelta(minutes=30))

                        session.add(new_user)
                        session.commit()

                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        try:
                            s.connect(('example.com', 80))
                            # Use the socket
                        finally:
                            s.close()

                        # Access properties only within the session
                        response_data = {'id': new_user.id, 'username': new_user.username, 'email': new_user.email,
                                         'password': new_user.password, 'vorname': new_user.vorname,
                                         'nachname': new_user.nachname,
                                         'is_super_user': new_user.is_super_user}

                        # Create a response with a cookie containing the token
                        # response = make_response('Registration successful')
                        # response.set_cookie('token', token, httponly=True, secure=True)

                    return response_data, 200
                else:
                    # Check if the data matches default values default valuse should not store in database
                    if (
                            data['id'] == 0
                            and data['username'] == "string"
                            and data['email'] != "string"
                            and data['password'] == "string"
                            and data['vorname'] == "string"
                            and data['nachname'] == "string"

                    ):
                        return {'error': 'Default values are not allowed.'}, 400

                    # Create a new superuser only if it's a superuser and has a valid email
                    if not data['is_super_user']:
                        if is_valid_email(data['email']):
                            return {'error': 'sorry!, Add E-mail Address for normal Users is not allowed,'}, 400
                        with Session(engine) as session:
                            # Check if the username already exists
                            existing_user = session.query(UserModel).filter(
                                or_(UserModel.vorname == data['vorname'], UserModel.username == data['username'],
                                    UserModel.nachname == data['nachname'])).first()

                            if existing_user:
                                # User with the same username already exists
                                return {'error': 'Username already exists'}, 400

                            # Generate a salt
                            salt = gensalt().decode("utf-8")

                            hashed_password = hashpw(data['password'].encode('utf-8'), salt.encode('utf-8'))

                            # Create a new user (non-superuser)
                            new_user = UserModel(
                                username=data['username'],
                                email=None,
                                password=hashed_password.decode("utf-8"),
                                vorname=data['vorname'],
                                nachname=data['nachname'],
                                salt=salt,
                                confirmation_token=None,
                                expiration_time=None,
                                confirmed=None,
                                is_super_user=False,
                            )

                            session.add(new_user)
                            session.commit()

                            # Access properties only within the session
                            response_data = {'id': new_user.id, 'username': new_user.username, 'email': new_user.email,
                                             'password': new_user.password, 'vorname': new_user.vorname,
                                             'nachname': new_user.nachname, 'is_super_user': new_user.is_super_user}
                            return response_data, 200
            except Exception as e:
                # Log the error for debugging
                print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'Add_user' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    from datetime import datetime

    def remove_expired_unconfirmed_users():
        with Session(engine) as session:
            now = datetime.utcnow()
            # Query for unconfirmed users where expiration_time is in the past
            expired_users = session.query(UserModel).filter(
                UserModel.confirmed == False,
                UserModel.is_super_user == True,
                UserModel.expiration_time < now
            ).all()

            # Delete each expired user individually
            for user in expired_users:
                session.delete(user)

            session.commit()

    scheduler = BackgroundScheduler()
    scheduler.add_job(remove_expired_unconfirmed_users, 'interval', days=1)
    scheduler.start()

    # Add a parser for parsing the user ID or username from the request
    delete_user_parser = reqparse.RequestParser()
    delete_user_parser.add_argument('user_id', type=int, help='ID of the user to delete')
    delete_user_parser.add_argument('username', type=str, help='Username of the user to delete')
    delete_user_parser.add_argument('user_id', '', type=str, help='ID or username of the user to delete', required=True)

    @ns_admin.route('/delete_user')
    class DeleteUserResource(Resource):

        @auth.login_required
        @ns_admin.expect(delete_user_parser)
        # @ns_admin.marshal_with(users_model) # optionanl field filter
        @require_role('superuser')
        def delete(self):
            try:
                # Parse the user ID or username from the request
                args = delete_user_parser.parse_args()
                user_id = args.get('user_id')
                username = args.get('username')

                # Use SQLAlchemy session to query and delete the user
                with Session(engine) as session:
                    if user_id:
                        user_to_delete = session.query(UserModel).get(user_id)
                    elif username:
                        user_to_delete = session.query(UserModel).filter_by(username=username).first()
                    else:
                        return {'error': 'User ID or username is required for deletion'}, 400

                    if user_to_delete:
                        session.delete(user_to_delete)
                        session.commit()
                        return {'message': f'User deleted successfully'}
                    else:
                        return {'error': 'User not found'}, 404

            except Exception as e:
                # Log the error for debugging
                print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

        # add token to header

    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'update_user' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'DELETE',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    # Add a parser for parsing the user data from the request
    update_user_parser = reqparse.RequestParser()
    update_user_parser.add_argument('user_id', type=int, help='ID of the user to update', required=True)
    update_user_parser.add_argument('username', type=str, help='New username for the user')
    update_user_parser.add_argument('email', type=str, help='New email for the user')
    update_user_parser.add_argument('password', type=str, help='New password for the user')
    update_user_parser.add_argument('vorname', type=str, help='New vorname for the user')
    update_user_parser.add_argument('nachname', type=str, help='New nachname for the user')
    update_user_parser.add_argument('is_super_user', type=bool, help='New superuser status for the user')

    @ns_admin.route('/update_user')
    class UpdateUserResource(Resource):
        @auth.login_required
        @ns_admin.expect(update_user_parser)
        @require_role('superuser')
        def put(self):
            try:
                # Parse the user data from the request
                args = update_user_parser.parse_args()
                user_id = args['user_id']

                # Use SQLAlchemy session to query and update the user data
                with Session(engine) as session:
                    user_to_update = session.query(UserModel).get(user_id)
                    if not user_to_update:
                        return {'error': f'User with ID {user_id} not found'}, 404

                    # Check and update password if new
                    if args.get('password'):
                        provided_password_hash = hashpw(args['password'].encode('utf-8'),
                                                        user_to_update.salt.encode('utf-8'))
                        if provided_password_hash != user_to_update.password.encode('utf-8'):
                            new_salt = gensalt()
                            new_hashed_password = hashpw(args['password'].encode('utf-8'), new_salt)
                            user_to_update.password = new_hashed_password.decode('utf-8')
                            user_to_update.salt = new_salt.decode('utf-8')

                    # Check and update email if new, and send verification email
                    if args.get('email') and args['email'] != user_to_update.email:
                        user_to_update.email = args['email']

                        # Generate a new confirmation token
                        confirmation_token = generate_confirmation_token()

                        # Calculate expiration time and store it along with the token
                        expiration_time = datetime.utcnow() + timedelta(days=1)
                        user_to_update.confirmation_token = confirmation_token
                        user_to_update.confirmation_token_expiration = expiration_time

                        # Send the confirmation email
                        send_confirmation_email(email=args['email'], confirmation_token=confirmation_token,
                                                expiration_time=expiration_time)

                    # Update other fields
                    for key, value in args.items():
                        if key not in ['password', 'email'] and value is not None:
                            setattr(user_to_update, key, value)

                    session.commit()

                    return {'message': f'User with ID {user_id} updated successfully'}

            except Exception as e:
                # Log the error for debugging purposes
                print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'update_user' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'put',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response



    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'options' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    @ns_admin.route('/update_user_username/<int:user_id>', doc={"description": "Update username of a user"})
    class UpdateUserUsernameResource(Resource):
        @auth.login_required
        @ns_admin.expect(users_model)
        @require_role('superuser')
        def patch(self, user_id):
            try:
                # Extract data from the request
                data = api.payload

                # Use SQLAlchemy session to query and update data
                with Session(engine) as session:
                    # Find the user by ID
                    user = session.query(UserModel).filter_by(id=user_id).first()

                    if not user:
                        return {'error': 'User not found'}, 404

                    # Update the username if provided in the request data
                    if 'username' in data:
                        user.username = data['username']

                    # Commit the changes to the database
                    session.commit()

                    # Return the updated user data
                    return {'id': user.id, 'username': user.username, 'vorname': user.vorname,
                            'nachname': user.nachname, 'email': user.email, 'password': user.password}
            except Exception as e:
                # Log the error for debugging purposes
                print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'update_user_username' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'PUT,DELETE',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })

        return response

    @ns_self_user.route('/User_Account')
    class AccDataResource(Resource):
        @auth.login_required
        def get(self):
            try:
                # Use SQLAlchemy session to query data
                with Session(engine) as session:
                    # Assuming the user information is stored in the g object during authentication
                    current_user_id = getattr(g, 'user_id', None)
                    # If the user_id is not available, return an error
                    if current_user_id is None:
                        return {'error': 'User information not available'}, 400
                    # Query the database for the information of the current user
                    current_user = session.query(UserModel).filter_by(id=current_user_id).first()
                    # If the current user is not found, return an error
                    if current_user is None:
                        return {'error': 'Current user not found'}, 404

                    # Return information for the current user
                    data_got = [{'id': current_user.id, 'username': current_user.username,
                                 'vorname': current_user.vorname, 'nachname': current_user.nachname,
                                 'email': current_user.email, 'password': current_user.password}]

                    return data_got
            except Exception as e:
                # Log the error for debugging purposes
                print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'User_Account' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    @ns_admin.route('/protected')
    class ProtectedResource(Resource):

        @auth.login_required
        @require_role('superuser')
        @ns_admin.marshal_with(users_model) # another optional field filter
        def get(self):
            try:
                # Use SQLAlchemy session to query data
                with Session(engine) as db_session:
                    super_users = db_session.query(UserModel).all()
                    data_got = [{'id': user.id,
                                 'username': user.username,
                                 'vorname': user.vorname,
                                 'nachname': user.nachname,
                                 'email': user.email,
                                 "is_super_user": user.is_super_user}
                                for user in super_users]
                return data_got
            except Exception as e:
                # Log the error for debugging purposes
                # print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'protected' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    @ns_admin.route('/unprotected')
    class UnProtectedResource(Resource):
        def get(self):
            try:
                # Use SQLAlchemy session to query data
                with Session(engine) as db_session:
                    super_users = db_session.query(UserModel).all()
                    data_got = [{'id': user.id,
                                 'username': user.username,
                                 'vorname': user.vorname,
                                 'nachname': user.nachname,
                                 'email': user.email,
                                 "is_super_user": user.is_super_user}
                                for user in super_users]
                return data_got
            except Exception as e:
                # Log the error for debugging purposes
                # print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'unprotected' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

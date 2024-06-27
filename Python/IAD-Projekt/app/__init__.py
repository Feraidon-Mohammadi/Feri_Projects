import os
from functools import wraps
from flask import Flask, g, make_response, url_for, render_template
from flask_migrate import Migrate
from flask_restx import Namespace, Api
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from jwt import decode, PyJWTError
from jwt.exceptions import ExpiredSignatureError
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from flask_bcrypt import Bcrypt
from app.config import DevelopmentConfiguration

from app.models.user_api_models import UserModel

from app.utils.email_utils import (is_confirmation_token_expired, is_valid_email, generate_confirmation_token,
                                   send_confirmation_email, send_support_email)
""" Odoo data """
from app.odoo_connector.odoo_connect import GetOdooData




class MyApplication:

    def __init__(self, config_class=DevelopmentConfiguration):
        self.app = Flask(__name__, template_folder="templates")
        self.config_class = config_class

        """ Odoo data for using unit test needed """
        # if GetOdooData == 200:
        #     self.instance_get_odoo_data = GetOdooData()
        # else:
        #     self.instance_get_odoo_data = None

        """ when odoo mit authentication connecting, need this,
        otherwise should use upper (if statement to by pass it)
        """
        self.instance_get_odoo_data = GetOdooData()

        self.setup_api()
        MyApplication.api = self.api  # Set the class variable

        self.db = SQLAlchemy()
        MyApplication.db = self.db

        self.bcrypt = Bcrypt(self.app)
        # self.mail = Mail(self.app) """ für die zukunft mail server hinzufugen"""
        
        self.auth = HTTPBasicAuth()
        # self.auth = MagicMock()
        self.token_auth = HTTPTokenAuth(scheme='Bearer')

        # database and Migration
        self.Base = declarative_base()

        self.configure_app()
        self.setup_db()
        self.create_namespaces()

        self.setup_routes()  # aufruf setup_routes zu register route
        self.setup_user_routes_external()

        # instances of authentication and token authenticator
        self.auth_manager = AuthenticationManager(self.auth, self.db, self.SECRET_KEY)
        self.auth_manager.setup_auth()
        self.token_authenticator = TokenAuthenticator(self.token_auth, self.SECRET_KEY, self.db)
        self.token_authenticator.setup_token_auth()
        
        """ Odoo data """
        self.setup_ns_odoo_routes_external()

    def configure_app(self):
        self.SECRET_KEY = self.app.config['SECRET_KEY']
        self.app.config.from_object(self.config_class)
        self.app.secret_key = self.app.config.get('SECRET_KEY', self.SECRET_KEY)

    def setup_api(self):
        description = ("""<marquee><h3>URP(Unternehmensressourcenplanung)</h3></marquee>\n<marquee direction="right">
        <h3>ERP(Enterprise Resource Planning)</h3></marquee>\n\n
        Middleware Secure API zur Pflege und Abfrage Daten von Odoo
        """)

        self.api = Api(self.app, version='1.0', title='IAD odoo API', description=description, doc="/home",
                       authorizations={
                           'apiKey': {
                               'type': 'apiKey',
                               'in': 'header',
                               'name': 'Authorization',
                           },
                           'basicAuth': {
                               'type': 'basic',
                           }
                       },
                       security=['BearerAuth', 'basicAuth'])


    def setup_db(self):
        migrate = Migrate(self.app, self.db)
        if os.environ.get('FLASK_ENV') != 'testing':
            database_file = 'database1.db'
            engine = create_engine(f'sqlite:///instance/{database_file}', echo=False)
            self.db.init_app(self.app)
            Migrate(self.app, self.db)
            with self.app.app_context():
                self.db.create_all()
                migrate.init_app(self.app, self.db)
                self.Base.metadata.create_all(bind=engine)
                self.db.session.commit()
            self.Base.metadata.create_all(bind=engine)
        else:
            database_file = 'atabase1.db'
            engine = create_engine(f'sqlite:///{database_file}', echo=False)
            self.db.init_app(self.app)
            Migrate(self.app, self.db)
            with self.app.app_context():
                self.db.create_all()
                migrate.init_app(self.app, self.db)
                self.Base.metadata.create_all(bind=engine)
                self.db.session.commit()
            self.Base.metadata.create_all(bind=engine)

    def create_namespaces(self):
        self.ns_odoo = Namespace("Odoo", description="Get data from Odoo")
        self.ns_admin = Namespace("Admin", description="Accounts Manager")
        self.ns_help = Namespace("Help", description="Reset Password")
        self.ns_self_user = Namespace("Profile", description="Profile Account Details")

        self.api.add_namespace(self.ns_odoo)
        self.api.add_namespace(self.ns_admin)
        self.api.add_namespace(self.ns_self_user)
        self.api.add_namespace(self.ns_help)
        self.setup_user_routes_external()
        
        """ Odoo data """
        self.setup_ns_odoo_routes_external()

    def setup_routes(self):
        @self.app.route('/confirm_email/<token>', methods=['GET'])
        def confirm_email(token):
            user = self.db.session.query(UserModel).filter_by(confirmation_token=token).first()

            if user and not user.confirmed:
                # Check if the confirmation token is still valid (not expired)
                if not is_confirmation_token_expired(user.expiration_time):
                    user.confirmed = True
                    self.db.session.commit()
                    return "Email confirmed successfully!"
                else:
                    return "Confirmation token has expired."
            else:
                return "Invalid confirmation token."

    """ Odoo data """
    def setup_ns_odoo_routes_external(self):
        from .resources.odoo_resources import setup_odoo_routes
        # Pass the necessary components as arguments
        from .models.odoo_models import create_odoo_models
        # Create models
        (odoo_model_measur_number, odoo_model_partner, odoo_model_special, odoo_model_measur, odoo_model_measure_name,
         odoo_model_all) = create_odoo_models(self.api)

        setup_odoo_routes(
            odoo_model_measur_number=odoo_model_measur_number,
            odoo_model_partner=odoo_model_partner,
            odoo_model_special=odoo_model_special,
            odoo_model_measur=odoo_model_measur,
            odoo_model_measure_name=odoo_model_measure_name,
            odoo_model_all=odoo_model_all,
            instance_get_odoo_data=self.instance_get_odoo_data,
            ns_odoo=self.ns_odoo,
            auth=self.auth,
            app=self.app,
        )

    def setup_user_routes_external(self):
        from .resources.users_resources import setup_api_routes
        from .resources.help_resources import setup_help_routes
        from .models.user_api_models import create_user_models

        users_model, current_user_model, help_model = create_user_models(self.ns_admin, self.ns_self_user, self.ns_help)
        setup_help_routes(
            ns_admin=self.ns_admin,
            ns_self_user=self.ns_self_user,
            ns_help=self.ns_help
        )
        setup_api_routes(
            app=self.app,
            auth=self.auth,
            api=self.api,
            ns_admin=self.ns_admin,
            ns_self_user=self.ns_self_user,
            ns_help=self.ns_help
        )


def create_app(config_class=DevelopmentConfiguration):
    setup = MyApplication(config_class)
    return setup.app


class AuthenticationManager:
    def __init__(self, auth, db, secret_key):
        self.auth = auth
        self.db = db
        self.secret_key = secret_key

    def setup_auth(self):
        @self.auth.verify_password
        def verify_password(username, password):
            # Verify the username and password against the database
            user = self.db.session.query(UserModel).filter_by(username=username).first()

            if user and user.check_password(password):
                g.user = user  # Set the user in the Flask global context (g)
                g.user_id = user.id  # Set the user ID in the Flask global context (g)
                token = user.generate_token()
                # print(f"Generated Token in verify pass: {token}")
                return True
            return False

        @self.auth.error_handler
        def auth_error(status):
            return {"message": "Access denied: Authentication failed", "status": status}, status

# berechtigung for user and super user
def user_has_required_role():
    user = getattr(g, 'user', None)
    if user and user.is_super_user:
        return True
    return False


# berechtigungs decorator
def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not user_has_required_role():
                return {'error': 'Permission denied'}, 403
            return func(*args, **kwargs)

        return wrapper

    return decorator


class TokenAuthenticator:
    def __init__(self, token_auth, secret_key, db):
        self.token_auth = token_auth
        self.secret_key = secret_key
        self.db = db

    def setup_token_auth(self):
        @self.token_auth.verify_token
        def verify_token(token):
            if not token:
                print("No token provided.")
                return False  # Deny access if no token is provided
            try:
                # Decode the token
                data = decode(token, self.secret_key, algorithms=["HS256"])
                # Retrieve the user based on the user ID in the token
                user_id = data.get('user_id')
                if user_id is None:
                    return None
                user = self.db.session.query(UserModel).get(user_id)
                return user
            except ExpiredSignatureError:
                # Explicitly handle expired tokens
                print("Token has expired.")
                return None
            except PyJWTError:
                print("A JWT error occurred.")
                return None



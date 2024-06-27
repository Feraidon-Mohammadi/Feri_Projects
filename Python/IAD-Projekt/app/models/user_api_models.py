import os
from datetime import datetime, timedelta
import jwt
from bcrypt import hashpw
from flask import current_app
from flask_restx import fields
from sqlalchemy import Column, String, Integer, DateTime, Boolean, create_engine
from sqlalchemy.orm import declarative_base

# für die erstellung des database enigin
Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'super_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=False)
    vorname = Column(String, nullable=False)
    nachname = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    confirmation_token = Column(String, unique=True, nullable=True)
    expiration_time = Column(DateTime, nullable=True)
    confirmed = Column(Boolean, nullable=True)
    is_super_user = Column(Boolean, default=False)

    def check_password(self, password):
        hashed_password = hashpw(password.encode('utf-8'), self.salt.encode('utf-8')).decode('utf-8')
        return self.password == hashed_password

    def generate_token(self, include_expiration=True):
        secret_key = current_app.config['SECRET_KEY']

        payload = {'user_id': self.id, 'username': self.username}

        if include_expiration and self.is_super_user:
            expiration_time = datetime.utcnow() + timedelta(hours=8)
            payload['exp'] = expiration_time
            self.expiration_time = expiration_time  # Set expiration time
        else:
            self.expiration_time = None

        token_generated = jwt.encode(payload, secret_key, algorithm='HS256')
        return token_generated


# Only create tables if not in testing environment
if os.environ.get('FLASK_ENV') != 'testing':
    database_file = 'database2.db'
    engine = create_engine(f'sqlite:///{database_file}', echo=False)
    # Create super_users when it not exists
    Base.metadata.create_all(bind=engine)


def create_user_models(ns_admin, ns_self_user, ns_help):

    users_model = ns_admin.model('SuperUser_schema', {
        'id': fields.Integer(readOnly=True, description='The unique identifier'),
        'username': fields.String(required=True, description='Username of the super user'),
        'email': fields.String(description='Email of the super user'),
        'password': fields.String(required=True, description='Password of the super user', attribute='password_hash'),
        'vorname': fields.String(required=True, description='First name of the super user'),
        'nachname': fields.String(required=True, description='Last name of the super user'),
        'is_super_user': fields.Boolean(default=False, description='Indicates if the user is a super user')
    })

    current_user_model = ns_self_user.model('Profil_Schema', {
        'username': fields.String(required=True, description='Username of the super user'),
        'email': fields.String(description='Email of the super user'),
        'vorname': fields.String(required=True, description='First name of the super user'),
        'nachname': fields.String(required=True, description='Last name of the super user'),
    })

    help_model = ns_help.model('help_Schema', {
        # 'email': fields.String(required=True, description='The email address of the user requesting help'),
        # static können die nutzer iad-email eingeben.
        
        'message': fields.String(required=True, description='The help message or request details'),
    })

    return users_model, current_user_model, help_model

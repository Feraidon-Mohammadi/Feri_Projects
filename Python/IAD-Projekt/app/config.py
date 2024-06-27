
class Configuration:

    # General Config
    SECRET_KEY = 'my_secret_key example'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database2.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Email Configuration für mail server für die zukunft...
    # MAIL_SERVER = 'smtp.example.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'your_email@example.com'
    # MAIL_PASSWORD = 'your_email_password'

class TestingConfiguration(Configuration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfiguration(Configuration):

    DEBUG = True


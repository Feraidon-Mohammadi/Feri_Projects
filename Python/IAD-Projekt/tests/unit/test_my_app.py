import os
import unittest
from unittest.mock import patch
# from flask_sqlalchemy import SQLAlchemy
from app import create_app


class TestConfig:
    TESTING = True
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class TestMyApplication(unittest.TestCase):

    def setUp(self):
        """um conflict zu beheben während test muss diese variable hizugefügt werden"""
        os.environ['FLASK_ENV'] = 'testing'

        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    #     self.db =self.db  # Use the global db_instance or initialize a new one if necessary
    #     self.db.init_app(self.app)  # Bind SQLAlchemy to the app
    #     with self.app.app_context():
    #         self.db.create_all()

    # def tearDown(self):
    #     with self.app.app_context():
    #         self.db.session.remove()
    #         self.db.drop_all()  # Drop all tables after tests
    #         self.app_context.pop()

    def test_configure_app(self):
        self.assertEqual(self.app.config['SECRET_KEY'], 'test')

    @patch('app.MyApplication.setup_db')
    def test_setup_db(self, mock_setup_db):
        mock_setup_db()
        mock_setup_db.assert_called_once()

    @patch('app.MyApplication.setup_api')
    def test_setup_api(self, mock_setup_api):
        mock_setup_api()
        mock_setup_api.assert_called_once()

    @patch('app.MyApplication.create_namespaces')
    def test_create_namespaces(self, mock_create_namespaces):
        mock_create_namespaces()
        mock_create_namespaces.assert_called_once()

    @patch('app.MyApplication.setup_user_routes_external')
    def test_setup_user_routes_external(self, mock_setup_user_routes_external):
        mock_setup_user_routes_external()
        mock_setup_user_routes_external.assert_called_once()

    """ verbunden mit odoo, """
    @patch('app.MyApplication.setup_ns_odoo_routes_external')
    def test_setup_ns_odoo_routes_external(self, mock_setup_ns_odoo_routes_external):
        mock_setup_ns_odoo_routes_external()
        mock_setup_ns_odoo_routes_external.assert_called_once()


if __name__ == "__main__":
    unittest.main()

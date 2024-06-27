import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, g, json
from flask_restx import Api, Namespace
from app.resources.users_resources import setup_api_routes
from app.resources.help_resources import setup_help_routes


def mock_login_required(func):
    return func


def mock_require_role(role):
    def decorator(func):
        return func
    return decorator


class TestAPIRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.auth = MagicMock()
        self.ns_admin = Namespace('admin')
        self.ns_self_user = Namespace('self_user')
        self.ns_help = Namespace('help')
        self.client = self.app.test_client()

        self.app.testing = True
        self.client = self.app.test_client()

        # Add namespaces to the API
        self.api.add_namespace(self.ns_admin)
        self.api.add_namespace(self.ns_self_user)
        self.api.add_namespace(self.ns_help)

    """ 
        Unprotected route successfully worked with unittest, 
        but protected route not work because login decoratore doesnt do json serialaizable data.  
    """
    @patch('app.resources.users_resources.create_engine')
    def test_Unprotected_resource(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_session = MagicMock()

        # Mocking the data returned by the database query
        mock_data = [{'id': 1, 'username': 'test'}]
        mock_session.query.return_value.all.return_value = mock_data

        mock_engine.__enter__.return_value = mock_session
        mock_create_engine.return_value = mock_engine

        # Setup API routes
        setup_api_routes(self.ns_admin, self.ns_self_user, self.ns_help, self.auth, self.app, self.api)

        # for debugging
        print("Registered Routes:", self.app.url_map)

        with self.app.test_client() as client:
            # Make a GET request to the protected route
            response = client.get('/admin/unprotected')

            # debugging
            print("Response Status Code:", response.status_code)

            # Assert the response status code
            self.assertEqual(response.status_code, 200)

            # Assert the response JSON data
            self.assertEqual(response.json, [])

    """ successfully worked user Profile Route """

    """ self account details if user not loged in """
    @patch('app.resources.users_resources.create_engine')
    def test_user_account_resource_not_logged_in(self, mock_create_engine):
        # Setup mock engine and session
        mock_engine = MagicMock()
        mock_session = MagicMock()

        # Mocking the data returned by the database query
        expected_user = MagicMock(id=1, username='testuser', vorname='Test',
                                  nachname='User', email='testuser@example.com',
                                  password='password')
        mock_session.query.return_value.filter_by.return_value.first.return_value = expected_user

        mock_engine.__enter__.return_value = mock_session
        mock_create_engine.return_value = mock_engine

        with self.app.app_context():
            with self.client:
                # Make a GET request to the /User_Account route
                response = self.client.get('/self_user/User_Account')

                # response status code is 404 indicating user not logged in
                self.assertEqual(response.status_code, 404)





if __name__ == '__main__':
    unittest.main()

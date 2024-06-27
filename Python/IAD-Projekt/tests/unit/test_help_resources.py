import unittest
from flask import Flask
from flask_restx import Api, Namespace
from unittest.mock import patch, MagicMock
from app.resources.help_resources import setup_help_routes
from app.utils.email_utils import send_support_email


class TestUserHelpResourceV2(unittest.TestCase):
    def setUp(self):
        """setup flask test client for external dependencies."""
        self.app = Flask(__name__, template_folder="templates")
        self.api = Api(self.app)

        with self.app.app_context():
            # Initialize your namespaces
            self.ns_help = Namespace('Help')
            self.ns_admin = Namespace('Admin')
            self.ns_self_user = Namespace('Profile')
            # Add namespaces to the API
            self.api.add_namespace(self.ns_help, path='/help')

            # Assuming setup_help_routes properly initializes routes using the provided namespaces
            setup_help_routes(self.ns_admin, self.ns_self_user, self.ns_help)

            # Initialize the test client
            self.test_client = self.app.test_client()

    @patch('app.utils.email_utils.render_template', return_value='Mocked email content')
    @patch('smtplib.SMTP_SSL')
    def test_send_support_email(self, mock_smtp, mock_render_template):
        # Configure the mock SMTP server to simulate a successful login and email send
        mock_smtp.return_value.__enter__.return_value.sendmail = MagicMock(return_value=True)
        # Attempt to send the email
        success = send_support_email("test@example.com", "Test message")
        # Assert the function succeeded
        self.assertTrue(success)
        # Assert render_template was called correctly
        mock_render_template.assert_called_once_with('help_form.html', message="Test message")

    patch('app.utils.email_utils.send_support_email', return_value=False)

    def test_help_request_failure(self):
        """Test help request with failed email sending."""
        response = self.test_client.post('/help/v2/help', json={'email': 'test@example.com', 'message': 'Help me!'})
        self.assertEqual(response.status_code, 404)

    def test_help_request_invalid_input(self):
        """Test help request with missing email or message."""
        response = self.test_client.post('/help/v2/help', json={'email': '', 'message': ''})
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()


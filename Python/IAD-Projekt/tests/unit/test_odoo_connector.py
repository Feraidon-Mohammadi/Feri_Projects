import os
import unittest
from unittest.mock import MagicMock, patch
from app.odoo_connector.odoo_connect import GetOdooData

# Einheitstest
class TestGetOdooData(unittest.TestCase):

    def setUp(self):
        """um conflict zu beheben während test muss diese variable hizugefügt werden"""
        os.environ['FLASK_ENV'] = 'testing'

        # Patch the ServerProxy within the context of where its used in the Get_Odoo_Data class
        patcher1 = patch('app.odoo_connector.odoo_connect.xmlrpc.client.ServerProxy')
        self.mock_server_proxy = patcher1.start()
        self.addCleanup(patcher1.stop)

        # Mock the authentication method to return a fake UID
        self.mock_common = MagicMock()
        self.mock_common.authenticate.return_value = 1
        self.mock_server_proxy.return_value = self.mock_common

        # Instantiate Get_Odoo_Data, which now uses the mocked ServerProxy
        self.odoo_connector = GetOdooData()

        # Replace the models attribute with a mock for testing the execute_kw method
        self.models_mock = MagicMock()
        self.odoo_connector.models = self.models_mock

    def test_get_data_by_model(self):
        # Define the expected result for the mock execute_kw method call
        expected_result = [{'id': 1, 'name': 'Test Partner'}]
        self.models_mock.execute_kw.return_value = expected_result

        """ such nach daten anhand des Odoo Model----> partner """
        partner = "res.partner"
        # Call the method under test
        result = self.odoo_connector.get_data_by_model(partner, [], ['name'], 10)

        # Assertions to verify the behavior and result
        self.assertEqual(result, expected_result)
        self.models_mock.execute_kw.assert_called_once_with(
            self.odoo_connector.odoo_db_info['database'],
            self.odoo_connector.uid,
            self.odoo_connector.odoo_db_info['password'],
            partner, 'search_read',
            [], {'fields': ['name'], 'limit': 10}
        )

if __name__ == '__main__':
    unittest.main()






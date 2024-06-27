import unittest
import requests


# intergrations test mit odoo
class TestOdooIntegration(unittest.TestCase):
    def setUp(self):
        # Set up the URL to your Flask application
        self.base_url = 'http://localhost:5000/api'
        # Optional: Set up any required headers, tokens, etc.
        self.headers = {'Content-Type': 'application/json'}
    
    
    def test_get_data_from_odoo(self):
        # Define the endpoint that interacts with Odoo
        endpoint = '/get_odoo_data'
        url = f'{self.base_url}{endpoint}'
        
        # Make a GET request to the Flask application
        response = requests.get(url, headers=self.headers)
        
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Optional: Check the structure of the response to ensure it's as expected
        # This depends on the expected response format from your Flask app
        data = response.json()
        self.assertIn('data', data)  # Example check
        # Further checks can be performed based on the specifics of your application
        # and the data it is supposed to retrieve from Odoo

if __name__ == '__main__':
    unittest.main()

import unittest

import requests
from flask import Flask
from flask_restx import Api
from app.models import odoo_models


class OdooModelsTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a Flask API instance for testing."""
        app = Flask(__name__)
        api = Api(app)

        (self.odoo_model_measur_number,
         self.odoo_model_partner, self.odoo_model_special, self.odoo_model_measur,
         self.odoo_model_measure_name,self.odoo_model_all) = odoo_models.create_odoo_models(api)


    def test_odoo_model_measur_number(self):
        """Test that the 'odoo_model_measur_number' model has the correct fields."""
        expected_fields = ["id", "name", "long_name", "start_date", "end_date",
                           "measure_type", "number", "display_name", "tag_ids",
                           "location_id", "special_day_ids"]
        for field in expected_fields:
            with self.subTest(model="odoo_model_measur_number", field=field):
                self.assertTrue(field in self.odoo_model_measur_number.keys(),
                                f"{field} is missing in odoo_model_measur_number")

    def test_odoo_model_measure_name(self):
        """Test that the 'odoo_model_measur_name' model has the correct fields."""
        expected_fields = ["id", "name"]
        for field in expected_fields:
            with self.subTest(model="odoo_model_measure_name", field=field):
                self.assertTrue(field in self.odoo_model_measure_name.keys(),
                f"{field} is missing in odoo_model_measur_number")

    def test_odoo_model_measur(self):
        """Test that the 'odoo_model_measur' model has the correct fields."""
        expected_fields = ["id", "name", "long_name", 'start_date', 'end_date', 'measure_type',
                           "number", "display_name", "tag_ids", 'location_id', "special_day_ids"]
        for field in expected_fields:
            with self.subTest(model="odoo_model_measur",field=field):
                self.assertTrue(field in self.odoo_model_measur.keys(),
                                f"{field} is missing in odoo_model_measur_number")

    def test_odoo_model_partner(self):
        """Test that the 'odoo_model_partner' model has the correct fields."""
        expected_fields = ["id", "name",  "display_name", "education_end_date", "education_school_day_total",
                           "forename", "city", "street", "phone"]
        for field in expected_fields:
            with self.subTest(model="odoo_model_partner",field=field):
                self.assertTrue(field in self.odoo_model_partner.keys(),
                                f"{field} is missing in odoo_model_partner")

    def test_odoo_model_special(self):
        """Test that the 'odoo_model_special' model has the correct fields."""
        expected_fields = ["id", "name", "display_name"]
        for field in expected_fields:
            with self.subTest(model="odoo_model_special",field=field):
                self.assertTrue(field in self.odoo_model_special.keys(),
                                f"{field} is missing in odoo_model_special")



    def test_create_odoo_models(self):
        """Test that the odoo_model_all structure contains the correct nested models and fields."""
        # Check that all expected nested models are present
        self.assertIn('nested_measur', self.odoo_model_all)
        self.assertIn('nested_special', self.odoo_model_all)
        self.assertIn('nested_partner', self.odoo_model_all)

        # Optionally, check some details of the nested models
        # This example checks if 'name' field is present in one of the nested models
        nested_measur_fields = self.odoo_model_all['nested_measur'].model.keys()
        self.assertIn('name', nested_measur_fields)


if __name__ == '__main__':
    unittest.main()


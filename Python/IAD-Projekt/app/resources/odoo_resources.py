import logging

from flask_restx import reqparse
from app import require_role
from flask import request, g, make_response, abort
from flask_restx import Resource, marshal
import traceback


def setup_odoo_routes(ns_odoo, app, auth, instance_get_odoo_data, odoo_model_measur_number, odoo_model_all,
                      odoo_model_measure_name, odoo_model_partner, odoo_model_special, odoo_model_measur):

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    class CustomError(Exception):
        def __init__(self, message, status_code):
            Exception.__init__(self)
            self.message = message
            self.status_code = status_code

    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        logging.error(f'Benutzerdefinierter Fehler: {error.message}')
        return {'message': error.message}, error.status_code

    """
     ***************** eine kurze erklärung für die oben genante parameter ***************

    : param ns_odoo: namespace nur für die odoo routes.
    : param app: application instance.
    : param auth: für die sicherheit maßnahmen anmeldung.
    : param instance_get_odoo_data: odoo connector class. damit kann man alle daten von odoo kriegen.
    : param odoo_model_measur_number:eine database model struktur damit man informationen anhang des Number finden kann.
    : param odoo_model_all: eine limitiertes route für die zukunft. um bestimmte daten von
        mehrere models zusammen in ein form zu haben.

    : param odoo_model_measure_name: daten mit aus model measure kriegen durch den  maßnahmen name.
    : param odoo_model_partner: limitierte daten aus database model partner.
    : param odoo_model_special: limitierte daten aus databaes model special days.
    : param odoo_model_measur: limitierte daten aus database model maßnahmen.
    """

    parser_string = reqparse.RequestParser()
    parser_string.add_argument('number', type=str, help='Number must be an String', location='args')
    
    parser_integer = reqparse.RequestParser()
    parser_integer.add_argument('number', type=str, help='Number must be an Interger', location='args')
    
    @ns_odoo.route('/Get_data_by_measur_number/<string:number>')
    class OdooDataByNumber(Resource):

        @auth.login_required
        @ns_odoo.doc(description="just authenticated users have access to this data", security='basicAuth')
        @ns_odoo.marshal_list_with(odoo_model_measur_number) # Optional fild für schema
        def get(self, number):
            try:
                measure = instance_get_odoo_data.get_data_measur()

                filtered_data = [item for item in measure if item.get('number') == number]

                # Assuming get_odoo_data returns a list of dictionaries
                if not filtered_data:
                    return {"message": "Data not found"}, 404

                return filtered_data, 200
            except CustomError as ce:
                # automatisch vom Fehlerbehandler behandelt
                raise ce
            except Exception as e:
                # Log the error for debugging purposes
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'Get_data_by_measur_number' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    """route by name"""
    @ns_odoo.route('/Get_data_by_measur_name/<string:measure_name>')
    class OdooDataName(Resource):
        @auth.login_required
        @ns_odoo.doc(description="just authenticated users have access to this data", security='basicAuth')
        @ns_odoo.marshal_list_with(odoo_model_measure_name)
        def get(self, measure_name):
            try:
                special_id = instance_get_odoo_data.get_data_special()
                
                filtered_data3 = [item for item in special_id if
                                  item.get('measure_name') == measure_name]

                if not filtered_data3:
                    return {"message": "Data not found"}, 404
                return filtered_data3
            except CustomError as ce:
                raise ce
            except Exception as e:
                #for debugging
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    @app.after_request
    def add_token_to_header(response):
        if hasattr(g, 'user') and 'Get_data_by_measur_name' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })

        return response

    """ 
        implemented for the future to find data according to name,id,number.
        each of those elements are available, if one of those find it will response the data, otherwise, not found.
    """
    # @ns_odoo.route("/Get_certainly_Data/<string:forename>/<string:number>/<int:id>")
    # class OdooDataCertainInofs(Resource):
    #     @auth.login_required
    #     @ns_odoo.doc(description="just authenticated users have access to this data", security='basicAuth')
    #     @ns_odoo.marshal_list_with(odoo_model_all)
    #     def get(self, forename, number, id):
    #         try:
    #             partner = instance_get_odoo_data.get_data_partner()
    #             measure = instance_get_odoo_data.get_data_measur()
    #
    #             if not partner and not measure:
    #                 return {"message": "Data not Found"}, 404
    #
    #             # Combine the data from both models
    #             combined_data = []
    #
    #             # Filter records based on provided parameters
    #             first_records = [item for item in partner if
    #                              item.get('forename') == forename or item.get('number') == number or item.get(
    #                                  "id") == id]
    #
    #             second_records = [item for item in measure if
    #                               item.get('forename') == forename or item.get('number') == number or item.get(
    #                                   "id") == id]
    #
    #             for record1 in first_records or second_records:
    #                 # Create a new dictionary for each item
    #                 combined_item = {}
    #
    #                 # Merge data from the first model
    #                 combined_item.update({
    #                     "forename": record1.get("forename"),
    #                     "city": record1.get("city"),
    #                     "street": record1.get("street"),
    #                     "phone": record1.get("phone"),
    #                 })
    #                 # Find the corresponding record in the second model
    #                 record2 = next((r for r in second_records if r["id"] == id), {})
    #                 # record2 = next((r for r in second_records if r["id"] == id), None)
    #                 if record2 is None:
    #                     return {"message": "Second model data not found for the given id"}, 404
    #                 # Merge data from the second model
    #                 combined_item.update(record2)
    #                 # Append the combined item to the result list
    #                 combined_data.append(combined_item)
    #
    #             if not combined_data:
    #                 return {"message": "Data not Found"}, 404
    #
    #             return combined_data
    #         except Exception as e:
    #             # Log the error for debugging purposes
    #             print(traceback.format_exc())  # or use logging
    #             return {"message": "Internal server error", "error": str(e)}, 500
    #
    # # add token to header
    # @app.after_request
    # def add_token_to_header(response):
    #     # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
    #     if hasattr(g, 'user') and 'Get_certainly_Data' in request.url:
    #         token = g.user.generate_token()
    #         response.headers['Authorization'] = f'Bearer {token}'
    #         response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
    #         response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    #         response.headers['X-Content-Type-Options'] = 'nosniff'
    #         response.headers['Content-Security-Policy'] = "default-src 'self'"
    #         response.headers.extend({
    #             'Access-Control-Allow-Origin': '*',
    #             'Access-Control-Allow-Methods': 'GET, OPTIONS',
    #             'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    #         })
    #     return response

    @ns_odoo.route("/Get_Special_id/<int:id>")
    class OdooDataByID(Resource):
        @auth.login_required
        @ns_odoo.doc(description="just Authenticated users have access to this route", security='basicAuth')
        def get(self, id):
            try:
                """ commented lines for the future implemented """
                # partner = instance_get_odoo_data.get_data_partner()
                # measure = instance_get_odoo_data.get_data_measur()
                special_id = instance_get_odoo_data.get_data_special()

                # filtered_data1 = [item for item in partner if item.get("id") == id]
                # filtered_data2 = [item for item in measure if item.get("id") == id]
                filtered_data3 = [item for item in special_id if item.get("id") == id]

                if not filtered_data3:
                    return {"message": "Data not found"}, 404
                return filtered_data3
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        if hasattr(g, 'user') and 'Get_Special_id' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    """
        multiple data model or many to one. 
        route by name ,id, number, the following route i implemented for the future to
        combine multiple models data and shows just one response.
    """
    @ns_odoo.route("/Get_all")
    class OdooAllData(Resource):

        @auth.login_required
        @ns_odoo.doc(description="just Authenticated users have access to this route", security='basicAuth')
        # @ns_odoo.marshal_list_with(odoo_model_all)
        def get(self):
            try:
                partner = instance_get_odoo_data.get_data_partner()
                measure = instance_get_odoo_data.get_data_measur()
                special_id = instance_get_odoo_data.get_data_special()

                """ if data are String format in models can be serialising with marshal here """
                # #Manually marshal data according to each model's schema
                # partner = marshal(partner, odoo_model_partner)
                # measure = marshal(measure, odoo_model_measur)
                # special_id = marshal(special_id, odoo_model_special)

                # Combine marshaled data into a single response
                response = {
                    "partners": partner,
                    "measures": measure,
                    "specials": special_id,
                }
                item = response["measures"][1],response["partners"][1],response["specials"][1]
                return item, 200
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        # Check if 'g' has the 'user' attribute and 'Get_users' is in the request URL
        if hasattr(g, 'user') and 'Get_all' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    @ns_odoo.route('/Add_Data_Odoo')
    class OdooDataAdd(Resource):

        @auth.login_required
        @require_role('superuser')
        @ns_odoo.doc(description="just Authenticated users have access to this route", security='basicAuth')
        @ns_odoo.expect(odoo_model_special)
        def post(self):
            try:
                data = request.json  # Get the new data from the request body
                new_partner = instance_get_odoo_data.add_partner_data(data)

                if new_partner:
                    return {'message': 'New partner added successfully', 'id': new_partner}, 201
                else:
                    # Adjust this part if there's a more specific way to identify failures
                    return {"message": "Failed to add new data"}, 400
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    # add token to header
    @app.after_request
    def add_token_to_header(response):
        if hasattr(g, 'user') and 'Add_Data_Odoo' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response

    @ns_odoo.route("/users/<string:forename>")
    class OdooUsersResource(Resource):
        @auth.login_required
        @ns_odoo.doc(description="just authenticated users have access to this data", security='basicAuth')
        #@ns_odoo.marshal_list_with(odoo_model_partner)
        def get(self, forename):
            try:
                special_id = instance_get_odoo_data.get_data_partner()

                filtered_data3 = [item for item in special_id if
                                  item.get('forename') == forename]

                if not filtered_data3:
                    return {"message": "Data not found"}, 404
                return filtered_data3
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    @app.after_request
    def add_token_to_header(response):
        if hasattr(g, 'user') and 'Get_data_by_measur_name' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })

        return response

    """ -------------- Warning!!!--------------------"""

    parser = reqparse.RequestParser()
    parser.add_argument('forename', type=str, required=True, help="Forename is required.")

    @ns_odoo.route('/Remove_Data_Odoo/<int:partner_id>')
    class OdooDataRemove(Resource):

        @auth.login_required
        @require_role('superuser')
        @ns_odoo.doc(description="Allows authenticated superusers to remove partner data by ID if the name matches",
                     security='basicAuth', params={'forename': 'A query parameter for the forename'})
        @ns_odoo.expect(parser)
        def delete(self, partner_id):
            # Parse the forename from query parameters
            args = parser.parse_args()
            forename = args['forename']
            try:
                # Attempt to find and verify the partner with the given ID and forename
                partner_exists, partner_matched = instance_get_odoo_data.verify_partner_by_id_and_forename(partner_id,
                                                                                                           forename)
                if not partner_exists:
                    return {"message": "Partner not found"}, 404
                elif not partner_matched:
                    return {"message": "Provided ID and forename do not match"}, 400

                # If the partner exists and the ID and forename match, proceed to delete
                deletion_success = instance_get_odoo_data.delete_partner_data(partner_id)

                if deletion_success:
                    return {'message': 'Partner removed successfully', 'id': partner_id}, 200
                else:
                    return {"message": "Failed to remove data"}, 400
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

    @app.after_request
    def add_token_to_header(response):
        if hasattr(g, 'user') and 'Remove_Data_Odoo' in request.url:
            token = g.user.generate_token()
            response.headers['Authorization'] = f'Bearer {token}'
            response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
            response.headers['X-Frame-Options'] = 'SAMEORIGIN'
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            response.headers.extend({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            })
        return response



    @ns_odoo.route("/Get_all_users_active_maßnahmen")
    class OdooAllUsersMassnahmenData(Resource):

        @auth.login_required
        @ns_odoo.doc(description="just Authenticated users have access to this route", security='basicAuth')
        #@ns_odoo.marshal_list_with(odoo_model_all)
        def get(self):
            try:
                partner = instance_get_odoo_data.get_data_partner()
                measure = instance_get_odoo_data.get_data_measur()
                special_id = instance_get_odoo_data.get_data_special()
                filtered_data3 = [item for item in special_id and measure and partner if
                                  item.get('active_education_plan_id') != False]

                """ if data are String format in models can be serialising with marshal here """


                item = filtered_data3
                print(item)
                return item, 200
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500





    @ns_odoo.route("/Get_all_users_gleich_maßnahmen/<string:measure_number>'")
    class OdooAllUsersGleich(Resource):

        @auth.login_required
        @ns_odoo.doc(description="just Authenticated users have access to this route", security='basicAuth')
        #@ns_odoo.marshal_list_with(odoo_model_all)
        def get(self,measure_number):
            try:
                partner = instance_get_odoo_data.get_data_partner()
                measure = instance_get_odoo_data.get_data_measur()
                special_id = instance_get_odoo_data.get_data_special()
                filtered_data3 = [item for item in special_id and measure and partner if
                                  item.get('measure_number') == measure_number]

                """ if data are String format in models can be serialising with marshal here """


                item = filtered_data3
                print(item)
                return item, 200
            except CustomError as ce:
                raise ce
            except Exception as e:
                logging.error(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

import socket
import traceback
from flask import request
from flask_restx import Resource
from app.models.user_api_models import create_user_models
from app.utils.email_utils import send_support_email


def setup_help_routes(ns_help, ns_self_user, ns_admin):

    """ User_Model """
    users_model, current_user_model, help_model = create_user_models(ns_help, ns_self_user, ns_admin)

    @ns_help.route('/v2/help')
    class UserHelpResourceV2(Resource):
        @ns_help.expect(help_model)
        def post(self):
            try: 
                data = request.json
                # an email address
                support_email = "......@example.com"
                email = support_email
                #email = data.get('email') # für static email kann use this
                message = data.get('message')

                # Ensure email and message are not None or empty
                if not email or not message:
                    return {'message': 'Email and message are required.'}, 400

                def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
                    try:
                        socket.create_connection((host, port), timeout=timeout)
                        return True
                    except OSError:
                        return False

                if not check_internet_connection():
                    return {'error': 'You are not connected to the Internet, Failed to send email'}, 500

                # Attempt to send the support email
                if send_support_email(email, message):
                    def use_socket_example():
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        try:
                            s.connect(('example.com', 80))
                        finally:
                            s.close()
                    return {'message': 'Your help request has been sent successfully.'}, 200
                else:
                    return {'message': 'Failed to send email.'}, 404

            except Exception as e:
                # Log the error for debugging purposes
                print(traceback.format_exc())
                return {"message": "Internal server error", "error": str(e)}, 500

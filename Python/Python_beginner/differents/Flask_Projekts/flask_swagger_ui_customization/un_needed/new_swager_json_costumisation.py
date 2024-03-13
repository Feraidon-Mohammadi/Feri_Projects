from flask import Flask, render_template
from flask_restx import Resource, Api, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
# api = Api(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
jwt = JWTManager(app)

# Mock users for demonstration (replace with your actual user storage)
users = {"username": "password"}

# Swagger UI customization
api = Api(app, doc="/swagger")

# Register a namespace
ns = api.namespace("my_namespace", description="My API")

# Custom Swagger UI HTML template
custom_swagger_template = """
    {% extends "swaggerui.html" %}
    {% block script %}
        {{ super() }}
        <script>
            // Customize the Swagger UI here
            $(document).ready(function () {
                // Add your customization code here
                // For example, you can add a button to the Swagger UI
                const authButton = $('<button>')
                    .text('Login')
                    .click(function() {
                        // Add logic to handle login button click
                        alert('Login button clicked');
                    });

                $('.topbar-wrapper .link').before(authButton);
            });
        </script>
    {% endblock %}
"""

# Route to serve the customized Swagger UI
@app.route("/swagger", endpoint="swagger_ui")
def swagger_ui():
    return render_template("custom_swagger_ui.html")

# Your resource with authorization
@ns.route("/protected")
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {"logged_in_as": current_user}

# Your resource for login
@ns.route("/login")
class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username cannot be blank")
    parser.add_argument("password", type=str, required=True, help="Password cannot be blank")

    def post(self):
        data = self.parser.parse_args()
        username = data["username"]
        password = data["password"]

        # Mock user authentication (replace with your actual authentication logic)
        if username in users and users[username] == password:
            # Generate JWT token
            access_token = create_access_token(identity=username)
            return {"access_token": access_token}
        else:
            return {"message": "Invalid credentials"}, 401

if __name__ == "__main__":
    app.run(debug=True)
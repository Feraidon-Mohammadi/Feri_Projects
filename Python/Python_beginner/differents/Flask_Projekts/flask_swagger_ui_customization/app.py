import jwt
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.exceptions import BadRequestKeyError
from flask import Flask, render_template, session, request, jsonify, make_response

app = Flask(__name__)
users = []
app.config["SECRET_KEY"] = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" # result

################################################################################################################
# create a hash password for secret key
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example usage
user_password = "password"
hashed_password = hash_password(user_password)

################################################################################################################



def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"Alert!": "Token is missing!"})
        try:
            payload = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return jsonify({"Alert!":"invalid token!"})
    return decorated

######################## alternative of obene functions ############################################
# def token_required(func):
#     @wraps(func)
#     def decorated(*args, **kwargs):
#         token = request.args.get("token")
#         if not token:
#             return jsonify({"Alert!": "Token is missing!"}), 401  # Return a 401 Unauthorized status
#         try:
#             payload = jwt.decode(token, app.config["SECRET_KEY"])
#         except jwt.ExpiredSignatureError:
#             return jsonify({"Alert!": "Token has expired!"}), 401  # Return a 401 Unauthorized status
#         except jwt.InvalidTokenError:
#             return jsonify({"Alert!": "Invalid token!"}), 401  # Return a 401 Unauthorized status
#         return func(*args, **kwargs)
#     return decorated
###################################################################################################################




# Home
@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    elif session.get("logged_in"):
        return "logged in currently!"
    else:
        return render_template("login_form_template")




# public
@app.route("/public", methods=["GET", "POST"])
def public():
    if request.method == "GET":
        return jsonify({"message": "Welcome to my Dashboard"})
    elif request.method == "POST":
        # Handle POST request logic if needed
        return jsonify({"message": "Received a POST request"})
    else:
        return jsonify({"error": "Method not allowed"}), 405  # 405 Method Not Allowed status


# Authenticated
@app.route("/auth", methods=["GET", "POST"])
@token_required
def auth():
    if request.method == "GET":
        return "JWT is verified. Welcome to my page."
    elif request.method == "POST":
        # Your POST logic here
        return "Received a POST request."


# Register form
@app.route("/register", methods=["POST", "GET"])
def register():

    # return render_template('register.html')

    if request.method == "POST":
        # if not session.get("registered"):
        #     return render_template("register.html")
        # elif session.get("registered"):
        #     #session["registered"]=True





        data = request.form

        # check filed are empty or not
        if not all(field in data for field in ["username".strip(), "password".strip()] ):
            return jsonify({"Error": "input fields cannot be empty"}),400

        username = data["username"]
        password = data["password"]

        # check user is existed or is new
        for user in users:
            if user["username"] == username:
                return jsonify({"Error":"Username is already taken"}),400

        # Check if username and password are not empty
        if not username or not password:
            return jsonify({"Error": "Username and password cannot be empty"}), 400


        # hashing the secret password
        hash_password = hashlib.sha256(password.encode()).hexdigest()

        # store hashed password in memory or database +++++++++++++
        users.append({"username":username, "password":hash_password})

        return jsonify({"message":"Registeration successfull"}), 201
    return render_template('register.html')


# loging
@app.route("/login", methods=["POST", "GET"])
def login():
    try:
        username = request.form["username"]
        password = request.form["password"]
    except BadRequestKeyError:
        return make_response("Invalid request parameters", 400)

    if username =="feri1" and password == "password":
        session["logged_in"] = True
        token = jwt.encode({
            "user": username,
            "expiration": str(datetime.utcnow() + timedelta(seconds=60))
        }, app.config["SECRET_KEY"])
        return jsonify({"token": token})

    # Check if username and password are not empty
    elif not username or not password:
        return jsonify({"Error": "Username and password cannot be empty"}), 400
    else:
        return make_response("Unable to verify ", 403, {"WWW-Authenticate": "Basic realm='Authentication Failed!'"})


if __name__=="__main__":
    app.run(debug=True)






"""

# Example route for OpenAPI specifications
@app.route('/specs')
def specs():
    # Replace this with your actual OpenAPI specifications
    openapi_specifications = {
        "openapi": "3.0.0",
        "info": {
            "title": "Your API",
            "version": "1.0.0",
        },
        # Add more OpenAPI specifications as needed
    }
    return jsonify(openapi_specifications)




"""
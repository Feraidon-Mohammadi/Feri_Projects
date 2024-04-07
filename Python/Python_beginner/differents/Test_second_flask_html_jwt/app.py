import jwt
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.exceptions import BadRequestKeyError
from hash_file import result
from flask import Flask, render_template, session, request, jsonify, make_response

app = Flask(__name__)
app.config["SECRET_KEY"] = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1f5e4r2id8"

# result

import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example usage
user_password = "password"
hashed_password = hash_password(user_password)
print(hashed_password)




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

######################## alternative of upper functions ############################################
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
@app.route("/home")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    elif session.get("logged_in"):
        return "logged in currently!"
    else:
        return render_template("login_form_template")


# public
@app.route("/public")
def public():
    return "for public"

# Authenticated
@app.route("/auth", methods=["GET", "POST"])
@token_required
def auth():
    if request.method == "GET":
        return "JWT is verified. Welcome to my page."
    elif request.method == "POST":
        # Your POST logic here
        return "Received a POST request."



# loging instead
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
            "expiration": str(datetime.utcnow() + timedelta(seconds=10))
        }, app.config["SECRET_KEY"])
        return jsonify({"token": token})
    else:
        return make_response("Unable to verify ", 403, {"WWW-Authenticate": "Basic realm='Authentication Failed!'"})








if __name__=="__main__":
    app.run(debug=True)






##### instead #########



# ######################## login ###########################################
# @app.route("/login", methods=["POST"])
# def login():
#     if request.form["username"] and request.form["password"] == "password":
#         session["logged_in"] =True
#         token = jwt.encode({
#         "user":request.form["username"],
#         "expiration":str(datetime.utcnow() + timedelta(seconds=120))
#
#         },
#             app.config["SECRET_KEY"])
#         return jsonify({"token":token.decode("utf-8")})
#     else:
#         return make_response("unable to verify", 403,{"WWW-Authenticate":"Basic realm:'Authentication Failed!'"})
#######################################################################


######## instead of login ########################




############################# instead of this method  ##############################################

# if request.method == "POST":
#         try:
#             username = request.form["username"]
#             password = request.form["password"]
#         except BadRequestKeyError:
#             return make_response("Invalid request parameters", 400)
#
#         if username == "feri1" and password == "password":
#             session["logged_in"] = True
#             token = jwt.encode({
#                 "user": username,
#                 "expiration": str(datetime.utcnow() + timedelta(seconds=10))
#             }, app.config["SECRET_KEY"])
#             return jsonify({"token": token})
#         elif "logout" in request.form:
#             session.pop('logged_in', None)
#             session.pop('username', None)
#             return make_response("Logout successful", 200)
#         else:
#             return make_response("Unable to verify", 403, {"WWW-Authenticate": "Basic realm='Authentication Failed!'"})
#     else:
#         return """
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Login</title>
#         </head>
#         <body>
#             <form action="/login" method="POST">
#                 <input type="text" name="username" placeholder="Username"><br><br>
#                 <input type="password" name="password" placeholder="Password"><br><br>
#                 <input type="submit" value="Login">
#             </form>
#         </body>
#         </html>
#         """
from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message
import random
import string


"""
## after run this file should run Gui i did kivy ,
"""


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'xxxxxxxxxxxxx@gmail.com'  # Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'rxyjkbrltnnfjegraipl'  # Replace with your Gmail password

mail = Mail(app)

users = {}  # User database (you should use a proper database in production)

def generate_confirmation_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    if email in users:
        return "User already registered!"

    confirmation_token = generate_confirmation_token()
    users[email] = {'confirmed': False, 'confirmation_token': confirmation_token}

    send_confirmation_email(email, confirmation_token)

    return "Registration successful! Check your email for confirmation."

@app.route('/confirm/<token>')
def confirm(token):
    email = next((email for email, user in users.items() if user['confirmation_token'] == token), None)

    if email:
        users[email]['confirmed'] = True
        return "Confirmation successful! You can now log in."
    else:
        return "Invalid confirmation token."

def send_confirmation_email(email, token):
    confirm_url = f"http://localhost:5000/confirm/{token}"
    msg = Message('Confirm your registration', sender='your@gmail.com', recipients=[email])
    msg.body = f"Click the following link to confirm your registration: {confirm_url}"
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
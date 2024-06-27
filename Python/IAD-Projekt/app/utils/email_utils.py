import re
import secrets
import smtplib
import socket
import ssl
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr

from flask import url_for, render_template


# """ email connection  """

def is_valid_email(email):
    """Check if the email address is a valid RFC 5321 address."""
    if not email:
        return False
    email_address = parseaddr(email)[1]
    if not email_address:
        return False
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email_address) is not None


def send_confirmation_email(email, confirmation_token, expiration_time):
    if not is_valid_email(email):
        # Log the invalid email scenario or handle it as needed
        print(f"Invalid email address: {email}")
        return

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    mail_server = "-------------@gmail.com"  # Corrected email address
    password = "----------"  # App password, generat a password trough email with 2 factory authenticathor its possible to generat an app key.and use it here
    """xxxxxxxxxxxxxxxxxxxxx""" # somthing like this, so long is the gen key.

    confirmation_link = url_for('confirm_email', token=confirmation_token, _external=True)
    logo_url = url_for('static', filename='img.png', _external=True)  # Generate the logo URL

    # Create a MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = "IAD GmbH <meilserver@gmail.com>"
    msg['To'] = email
    msg['Subject'] = "Confirmation Email"

    # 1- Create the HTML version of  message entweder mit render template oder wie unten mit jinja forma
    # html = render_template('email_form.html', confirmation_link=confirmation_link, logo_url=logo_url)

    # 2- ich würde wurde gerne jinja verwenden
    html = f"""\
    <html>
        <head>
            <style>
            .header {{
                padding: 20px;
                text-align: center;
                background: linear-gradient(to right, #ff9966, #ff5e62);
                color: white;
                font-size: 24px;
            }}
            
            .footer {{
                padding: 20px;
                text-align: center;
                background: linear-gradient(to right, #ff9966, #ff5e62);
                color: white;
                font-size: 24px;
            }}
            
            .button {{
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #fff;
            background-color: #4CAF50;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
            }}
            
            .button:hover {{background-color: #3e8e41}}
            
            .button:active {{
            background-color: #3e8e41;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
            }}
            
            .colorful-window {{
            background-color: #f2f2f2; /* Light grey background */
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            }}
            </style>
        </head>
      <body>
        <div class="header">

            <img src="{logo_url}" alt="Logo" style="max-width:100px;">
            Welcome!
        </div>

        <div class="colorful-window">
          <p>Hi Dear user,</p>
          <p>Thank you for signing up! To complete your registration, please click on the following link to confirm your
           email address:</p>
          <a href="{confirmation_link}" class="button">Confirm Email</a>

          <p>If you didn't sign up for our service, please ignore this email.</p>
          <a href="https://www.iad.de/standorte/erfurt">more infos in our website</a>

          <p>Regards,<br>iad GmbH</p>
        </div>

        <div class="footer">
            Thank you for using our Services!,
        </div>

      </body>
    </html>
    """
    # Define the plain text body
    header = f""" Confirm the following link,"""

    # Attach the message body. This time, both plain and HTML versions
    part1 = MIMEText(header, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Use the smtplib code to send the email within a try-except block for error handling
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(mail_server, password)
            server.sendmail(mail_server, email, msg.as_string())
    except (socket.gaierror, socket.error):
        return "Internet connection error", 503
    except smtplib.SMTPAuthenticationError:
        return "Authentication error", 401
    except Exception as e:
        print(f"Error sending confirmation email: {e}")
        return "Email sending error", 500


# send support message
def send_support_email(email, message):
    if not is_valid_email(email):
        # Log the invalid email scenario or handle it as needed
        print(f"Invalid email address: {email}")
        return

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    mail_server = "-------------@gmail.com"  # Corrected email address 
    password = "--------------"  # App password, generat a password trough upper email with 2 factory authenticathor its possible to generat an app key.and use it here
    """a long code will be like 16-25 char """

    # Create a MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = "IAD GmbH <meilserver@gmail.com>"
    msg['To'] = email
    msg['Subject'] = "Help Request Email"

    html = render_template('help_form.html', message=message)

    # Define the plain text part (optional, could include the same message or a summary)
    plain_text = "You have received a help request."

    # Attach the message body. This time, both plain and HTML versions
    part1 = MIMEText(plain_text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Use the smtplib code to send the email within a try-except block for error handling
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(mail_server, password)
            server.sendmail(mail_server, email, msg.as_string())
            return True
    except Exception as e:
        print(f"Error sending confirmation email: {e}")
        return False


def is_confirmation_token_expired(expiration_time):
    now = datetime.utcnow()
    return now > expiration_time


# generate a random uinque token to verify email address
def generate_confirmation_token():
    """Generate a unique confirmation token."""
    return secrets.token_urlsafe(32)


def send_password_reset_email(email, reset_token):
    if not is_valid_email(email):
        # Log the invalid email scenario or handle it as needed
        print(f"Invalid email address: {email}")
        return

    # Your SMTP settings
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    mail_server = "-------------@gmail.com"  # Corrected email address 
    password = "--------------"  # App password, generat a password trough upper email with 2 factory authenticathor its possible to generat an app key.and use it here

    # Create the password reset link
    reset_link = url_for('reset_password', token=reset_token, _external=True)

    # Email subject
    subject = "Password Reset Requested"

    # Create the HTML for the email
    html = f"""\
    <html>
        <head>
            <style>
                /* Your existing styles */
            </style>
        </head>
        <body>
            <div class="header">
                <img src="{"<h1>IAD</h2>"}" alt="Logo" style="max-width:100px;">
                Password Reset Request
            </div>
            <div class="colorful-window">
                <p>Hi,</p>
                <p>You have requested to reset your password. Please click on the link below to set a new password:</p>
                <a href="{reset_link}" class="button">Reset Password</a>
                <p>If you did not request a password reset, please ignore this email or contact support if you have 
                concerns.</p>
                <p>Regards,<br>iad GmbH</p>
            </div>
            <div class="footer">
                If you’re having trouble clicking the "Reset Password" button, copy and paste the URL below into 
                your web browser: {reset_link}
            </div>
        </body>
    </html>
    """

    # Define the plain text body
    text_body = "Please click the link below to reset your password: {}".format(reset_link)

    # Create a MIMEMultipart message
    msg = MIMEMultipart('alternative')
    msg['From'] = "IAD GmbH <meilserver@gmail.com>"
    msg['To'] = email
    msg['Subject'] = subject

    # Attach the message body
    part1 = MIMEText(text_body, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Use smtplib to send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(mail_server, password)
            server.sendmail(mail_server, email, msg.as_string())
    except Exception as e:
        print(f"Error sending password reset email: {e}")
        return False

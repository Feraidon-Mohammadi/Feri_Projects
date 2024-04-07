# Download the helper library from https://www.twilio.com/docs/python/install
# test twilio : AC297a57f995d204a606e52ff9f2e3r8i23e74



import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

phone_number = client.messaging \
    .v1 \
    .services('MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .phone_numbers \
    .create(
    phone_number_sid='PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    )

print(phone_number.sid)



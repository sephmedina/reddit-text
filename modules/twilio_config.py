"""
twilio_config.py

contains info needed for connecting with twilio

"""
from twilio.rest import Client
from twilio import twiml

# Account Sid and Auth Token located @ twilio.com/console

# setting up client
account_sid = ''
auth_token = ''
twilio_client = Client(account_sid, auth_token)

message_from = '' # phone nunber from my Twilio account
message_to = '' # my phone number, linked with my Twilio account





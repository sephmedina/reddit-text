"""
twilio_config.py

contains info needed for connecting with twilio

"""
from twilio.rest import Client
from twilio import twiml

# Account Sid and Auth Token located @ twilio.com/console

'''
# Joseph's:

# setting up client
account_sid = 'AC9e499ccdc3dba56e792badace369f027'
auth_token = '8028610737dd11cfdd068efef3883197'
twilio_client = Client(account_sid, auth_token)

message_from = '+15103450626 ' # phone nunber from my Twilio account
message_to = '+15109782799' # my phone number, linked with my Twilio account

'''


# Josh's:

# setting up client
account_sid = 'AC1f57610bfdff264a070084207e065d24'
auth_token = 'e1512dbcc7fd6ae1accf88f01599e513'
twilio_client = Client(account_sid, auth_token)

message_from = '+14153606487' # phone nunber from my Twilio account
message_to = '+15102609647' # my phone number, linked with my Twilio account





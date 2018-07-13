"""
twilio_sms.py

contains functions that use the twilio library

"""
from modules.twilio_config import twilio_client, message_to, message_from
from twilio.twiml.messaging_response import MessagingResponse

def send_message(message_body : str) -> None:
	""" sends the message """
	twilio_client.messages.create(
	                              body = message_body,
	                              from_ = message_from,
	                              to = message_to)

def check_message(message: str) -> str:
	""" checks if the message exceeds 1600 characters. 
		if so, returns sends the first 1600 and returns
		the rest. Otherwise, just returns the given msg.
	"""
	if len(message) > 1600:
		send_message(message[:1500])
		message = message[1500:]

	return message

def twiml_response(message: str) -> str:
	"""	Returns a Twiml Response back to Twilio to send to Phone Number """
	final_message = check_message(message)
	response = MessagingResponse()
	response.message(final_message)
	return str(response)



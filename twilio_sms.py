from twilio_config import twilio_client, message_to, message_from
from twilio.twiml.messaging_response import MessagingResponse

def send_message(message_body : str) -> None:
	# sends the message
	message = twilio_client.messages.create(
	                              body = message_body,
	                              from_ = message_from,
	                              to = message_to)
def print_message():
	# prints last 5 messages, for testing
	messages = twilio_client.messages.list()
	for i in range(5):
		print(messages[i].body)

def send_twiml_response(message):
	"""	Returns a Twiml Response back to Twilio to send to Phone Number """
	response = MessagingResponse()
	response.message(message)
	#IF MESSAGE > 1600, BREAK DOWN INTO MORE POSTS. SEND FIRST AS TWIML, USE SEND_MESSAGE FOR REST
	return str(response)

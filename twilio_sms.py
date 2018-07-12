from twilio_config import twilio_client, message_to, message_from
from twilio.twiml.messaging_response import MessagingResponse

def send_message(message_body : str) -> None:
	# sends the message
	message = twilio_client.messages.create(
	                              body = message_body,
	                              from_ = message_from,
	                              to = message_to)

def print_message():
	# printing messages

	# prints last 5 messages, for testing
	messages = twilio_client.messages.list()
	for i in range(5):
		print(messages[i].body)

def get_messages():
	return twilio_client.messages.list()

def response(message):
	response = MessagingResponse()
	response.message(message)
	return str(response)

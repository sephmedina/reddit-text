from twilio.rest import Client

def send_message(message_body : str) -> None:
	# Account Sid and Auth Token located @ twilio.com/console

	# setting up client
	account_sid = 'AC1f57610bfdff264a070084207e065d24'
	auth_token = 'e1512dbcc7fd6ae1accf88f01599e513'
	client = Client(account_sid, auth_token)

	message_from = '+14153606487' # phone nunber from my Twilio account
	message_to = '+15102609647' # my phone number, linked with my Twilio account

	# sends the message
	message = client.messages.create(
	                              body = message_body,
	                              from_ = message_from,
	                              to = message_to)

	# proof that message was sent
	print(message.sid)

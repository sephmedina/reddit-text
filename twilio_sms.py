from twilio.rest import Client

def send_message(message_body : str) -> None:
	# Account Sid and Auth Token located @ twilio.com/console

	# setting up client
	account_sid = 'AC9e499ccdc3dba56e792badace369f027'
	auth_token = '8028610737dd11cfdd068efef3883197'
	client = Client(account_sid, auth_token)
	message_from = '+15103450626 ' # phone nunber from my Twilio account
	message_to = '+15109782799' # my phone number, linked with my Twilio account

	# sends the message
	message = client.messages.create(
	                              body = message_body,
	                              from_ = message_from,
	                              to = message_to)

	# proof that message was sent
	print(message.sid)

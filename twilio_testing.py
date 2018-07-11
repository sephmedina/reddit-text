import reddit
import twilio_sms

# testing twilio
def test():
	send = False
	if send:
		post_info = reddit.get_post_info('smashbros',1,2,'hot')
		twilio_sms.send_message(post_info)

	twilio_sms.print_message()
	

if __name__ == '__main__':
	test()

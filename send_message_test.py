import twilio_sms
import reddit

def main():
	send = True
	if send:
		top_post = reddit.get_post_info('smashbros',1,2,'hot');
		twilio_sms.send_message(top_post);

#running server/application
if __name__ == '__main__':
	main()

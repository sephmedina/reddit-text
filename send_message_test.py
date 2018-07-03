import twilio_sms
import reddit

def main():
	send = False
	if send:
		top_post = reddit.get_top_post();
		twilio_sms.send_message(top_post);

#running server/application
if __name__ == '__main__':
	main()

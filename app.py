from flask import Flask, request, render_template
import twilio_sms
import reddit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	"""Landing Page"""
	send = False
	if send:
		top_post = reddit.get_post_info('UCI',1,1,'hot') # look at reddit.py
		twilio_sms.send_message(top_post)
	return render_template('index.html', request=request.method)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
	"""Return posts in user-submitted subreddit"""
	if request.method == 'POST':
		subreddit = request.values.get['Body']
		reddit_post = reddit.get_post_info(subreddit, 2, 0, "hot")
		response = twilio_sms.response(reddit_post)
		return response

	else:
		return render_template('sms.html')

#running server/application
if __name__ == '__main__':
	'''
	Workflow
	1)Listen for SMS asking for reddit post - Twilio
	2)Grab top post from subreddit (UCI) - Reddit
	3)Send Message through twilio using the post as an argument - twilio + reddit
	'''
	app.run()

from flask import Flask, request, render_template
import twilio_sms
import reddit

#routing
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
	"""Landing Page"""
	send = False
	if send:
		top_post = reddit.get_top_post()
		twilio_sms.send_message(top_post)
	return render_template('index.html', request=request.method)

#running server/application
if __name__ == '__main__':
	'''
	Workflow
	1)Listen for SMS asking for reddit post - Twilio
	2)Grab top post from subreddit (UCI) - Reddit
	3)Send Message through twilio using the post as an argument - twilio + reddit
	'''
	app.run(debug=True)

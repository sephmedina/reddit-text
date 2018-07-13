from flask import Flask, request, render_template
from twilio_sms import send_twiml_response
from reddit import get_post_info

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
	"""Landing Page"""
	return render_template('index.html')

@app.route("/sms", methods=['POST'])
def sms():
	"""Return posts in user-submitted subreddit"""
	subreddit = request.values.get('Body')	#get subreddit
	posts = get_post_info(subreddit, 2, 1, "hot") #get posts
	#Posts are formatted in TwiML to Twilio, then sent to original sender
	return send_twiml_response(posts)

#running server/application
if __name__ == '__main__':
	app.run()

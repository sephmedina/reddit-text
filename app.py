"""
app.py

The script used for deploying this bot
"""
from flask import Flask, request, render_template
from modules.twilio_sms import twiml_response
from modules.reddit import get_post_info
from modules.checker import tutorial_message, check_info, parse_message

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	"""Landing Page"""
	return render_template('index.html')

@app.route("/sms", methods=['POST'])
def sms():
	"""Return posts in user-submitted subreddit"""

	response = request.values.get('Body')	# user message
	subreddit, number, category = parse_message(response) # parse the message
	info = tutorial_message # by default, message to be sent is the tutorial message
	
	# if info is in correct format, get reddit post info
	if check_info(subreddit, number, 1, category):
		info = get_post_info(subreddit, int(number), 1, category)

	# info is formatted in TwiML to Twilio, then sent to original sender
	return twiml_response(info)

# running server/application
if __name__ == '__main__':
	app.run()

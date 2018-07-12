from flask import Flask, request, render_template
import twilio_sms
import reddit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	"""Landing Page"""
	return render_template('index.html', request=request.method)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
	"""Return posts in user-submitted subreddit"""
	if request.method == 'POST':
		#print(request.values.get['Body'])
		subreddit = request.values.get('Body')
		reddit_post = reddit.get_post_info(subreddit, 2, 1, "hot")
		response = twilio_sms.response(reddit_post)
		return str(response)
	else:
		return render_template('sms.html')

#running server/application
if __name__ == '__main__':
	app.run(debug=True)

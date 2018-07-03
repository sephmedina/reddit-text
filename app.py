from flask import Flask, request, render_template
import twilio_sms


#routing
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():

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

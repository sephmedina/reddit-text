from flask import Flask, request, render_template
import tweepy


#jinja section
#twitter section


auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  #initializes API

#routing
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', request=request.method)

@app.route('/maps/', methods=['GET','POST'])
def maps():
    return render_template('maps.html')

@app.route('/about/', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/twitter/', methods=['GET','POST'])
def twitter():
    tweets = []
    for status in tweepy.Cursor(api.user_timeline, id='kanyewest').items(15): #parameters should be placed in Cursor constructor
        tweets.append(status.text)
    return render_template('twitter.html', tweets=tweets)


#running server/application
if __name__ == '__main__':
    app.run(debug=True)


#https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use # killing server
#TODO:
#1)implement navbar with css
#Done for now
    #2)implement open data API
#print out data from api - DONE
        #make marker on google maps with API
    #3) look into xmlHttpRequest
    #4) https://getbootstrap.com/docs/3.3/getting-started/
    #5) can print out text next steps
    #6) keep search search
        #make new div specified for incoming searches
        #make marker on google maps with address from searches
        #Error message when search is bad






    #soundcloud for fun https://developers.soundcloud.com/docs/api/guide#authentication
    #idea - group signups for park cleanup
#    restaurant inspections - https://www.opendatanetwork.com/dataset/data.cityofberkeley.info/iuea-7eac

#https://www.w3schools.com/css/css3_animations.asp
#https://www.w3schools.com/css/css3_transitions.asp
#https://www.opendatanetwork.com/search?q=berkeley
#visual of traffic stops in berkeley. implement with google maps to find route with no traffic

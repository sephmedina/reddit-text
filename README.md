# reddit-text

**Reddit Texting Service:**

Text a subreddit to the service’s phone number and receive a text message back, consisting of posts from the requested subreddit. 

-------------------------------------------------------------------------

**Use Case:**

User is able to get their latest information from their favorite subreddits in seconds, without needing to access the internet.

-------------------------------------------------------------------------
**Examples Cases:**

# 1

User texts "UCI"

User receives a text detailing the top post from the UCI subreddit.

# 2

User texts "college 3"

User receives a text detailing the top 3 posts from the college subreddit.

# 3

User texts "news 3 new"

User receives a text detailing the newest 3 posts from the news subreddit.

# 4 

**Error Case**

User texts "Hi how are you doing today"

User receives a text detaiing what our service does (user needs to text something like the 3 examples above)

-------------------------------------------------------------------------


**This project uses Flask, Praw, and Twilio.** 

**Deployed @ http://reddittextapp.pythonanywhere.com/**

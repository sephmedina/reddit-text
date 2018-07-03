import praw

def get_reddit_object() -> 'reddit object':
	CLIENT = 'NkTmzbz9_Akg5w'
	SECRET = 'vAeI7tarAe2MQdhUYZZI4NCkWls'
	BOT_NAME = 'JoshSearchBot'
	BOT_PASSWORD = 'JoshSearchBot'
	AGENT = 'created by JOSH'
	REDDIT = praw.Reddit(client_id = CLIENT, client_secret = SECRET, username = BOT_NAME, password = BOT_PASSWORD, user_agent = AGENT)

	return REDDIT

def get_top_post() -> 'url, title, and body of top post':
	reddit = get_reddit_object()
	hot = reddit.subreddit('UCI').hot()
	sub = None
	for s in hot:
		sub = s
		break
	return sub.url + '\n' + sub.title + '\n' + sub.selftext

# testing:
print(get_top_post())
import praw

client = 'NkTmzbz9_Akg5w'
secret = 'vAeI7tarAe2MQdhUYZZI4NCkWls'
bot_name = 'JoshSearchBot'
bot_password = 'JoshSearchBot'
agent = 'created by JoshTavasso and SephMedina'

reddit_obj = praw.Reddit(client_id = client, 
						 client_secret = secret, 
						 username = bot_name, 
						 password = bot_password, 
						 user_agent = agent)


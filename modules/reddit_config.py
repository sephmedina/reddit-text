"""
reddit_config.py

contains info needed to connect with reddit

"""
import praw

reddit_obj = praw.Reddit(client_id = client, 
						 client_secret = secret, 
						 username = bot_name, 
						 password = bot_password, 
						 user_agent = agent)


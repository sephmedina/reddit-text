"""
checker.py

Used for checking and parsing the user's message

"""

from modules.reddit_config import reddit_obj

"""
	Used when the user sends an invalid message, to 
	let them know how a message should be sent
"""
tutorial_message = """
Hi! Please send your message in the following format:
subreddit (space) # of posts (space) category.
Example: UCI 2 hot
This example asks us to get you the first 2 hot posts
in the UCI subreddit!
If you have no specification, just send a subreddit 
and we'll send over the first top post in the hot category!"
"""

def check_for_int(*args) -> bool:
	""" checks if the args given are positive ints """
	try:
		for arg in args:
			if int(arg) < 1:
				return False

	except ValueError:
		return False

	return True

def check_info(sub_name: str, number_of_posts: int, start_point: int, category: str) -> bool:
	""" checks user input, returning a boolean depending if it is correct or not """

	# this try/except block checks if the subreddict and category exist
	try:
		"""
			gets the url of the given subreddit's first post, given a category.
			this shouldn't crash, if the user input is correct.
		""" 
		eval("reddit_obj.subreddit('{}').{}()".format(sub_name,category)).next().url

	except:
		""" 
			if any error occured, something must be wrong 
			with subreddit/category
		"""
		return False

    # last bit of info to check; if the # of posts given is an int
	return check_for_int(number_of_posts, start_point)

def parse_message(user_message: str) -> ['subreddit', 'number', 'category']:
	""" user message should be in
		the form: 'subreddit number category'
		This function splits that message, 
		compiles it into a list, and returns it.
	"""
	user_message = user_message.split()

	""" if the length of the user message is
		greater than 3, the message is invalid
		by default, so we return an invalid list
	"""
	if len(user_message) > 3:
		return ['Invalid Subreddit', 'Invalid Number', 'Invalid Category']

	# if the length is <= 3:

	info = [user_message[0], 1, 'hot'] # default
	for i in range(len(user_message)):
		info[i] = user_message[i]
	
	return info
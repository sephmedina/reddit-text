import praw

def get_reddit_object() -> 'reddit object':
	''' Returns a Reddit object using info from the
		JoshSearchBot account
	'''
	client = 'NkTmzbz9_Akg5w'
	secret = 'vAeI7tarAe2MQdhUYZZI4NCkWls'
	bot_name = 'JoshSearchBot'
	bot_password = 'JoshSearchBot'
	agent = 'created by JoshTavasso and SephMedina'

	reddit_obj = praw.Reddit(client_id = client, client_secret = secret, username = bot_name, 
							password = bot_password, user_agent = agent)
	return reddit_obj

def get_post_info(sub_name: str, number_of_posts: int, start_point: int,  category: str) -> str:
	'''
	Retrieves desired post info from reddit.
	sub_name is a string representing the name of the subreddit to be searched in.
	numnber_of_posts is the number of posts wanted.
	start_point is the point in the list of posts to start at.
	category is the category to search in (such as hot or new)
	Returns a str with the info from the reddit posts desired
	'''

	# get a list of posts from a desired subreddit and category:
	reddit_obj = get_reddit_object()
	sub_list = eval("reddit_obj.subreddit('{}').{}()".format(sub_name,category))

	# sets the sub_list to the position desired
	for _ in range(start_point - 1):
		sub_list.next()

	'''
	iterates through the sub_list starting
	from the desired position and ends at 
	the number of posts desired.
	adds the post info to a str to be returned
	at the end
	'''
	post_counter = start_point
	str_to_return = ""
	for sub in sub_list:
		str_to_return += "Here is post #{} in the {} category on the {} subreddit".format(post_counter,category,sub_name)
		str_to_return += "\n\nURL:\n{}\n\nTITLE:\n{}\n\nBODY:\n{}\n\n".format(sub.url, sub.title, sub.selftext)
		if number_of_posts == 1:
			break
		else:
			post_counter += 1
			number_of_posts -= 1

	return str_to_return

	

# testing:
debug = False
if debug:
	print(get_post_info('UCI',2,2,'hot'))

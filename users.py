
#6y7LtOjoNEfe72g62kZfwtFHMWkQ8XsZvcQ8xZDe

import praw

outfile = open('users.html', 'w')

credentials = open('credentials', 'r')
client_id = credentials.readline().strip(' \t\n\r')
client_secret = credentials.readline().strip(' \t\n\r')

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='atlas_bot')

users = set()

# Manual entries:
users.add("MoonShinez");
users.add("Shovel_Ship");

for submission in reddit.subreddit('placeAtlas').new(limit=10000):
	users.add(submission.author.name)

users = list(users)
users = sorted(users, key=str.lower)

print(len(users))

for user in users:
	outfile.write("\t\t\t\t\t<a href=\"https://reddit.com/user/"+user+"\" target=\"_blank\">"+user+"</a>\n")
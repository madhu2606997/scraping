from facebook_scraper import get_posts

for post in get_posts('drguravareddy', pages=5):
	print(post)
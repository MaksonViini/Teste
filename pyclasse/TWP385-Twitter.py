from twitter_scraper import get_tweets
tweets = []
for i in get_tweets('mbl', pages=1):
    tweets.append(i)
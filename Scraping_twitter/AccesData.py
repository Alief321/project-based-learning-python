import tweepy
from tweepy import OAuthHandler


print("Hello World") 
consumer_key = '2aukMPlEiUdKvVfldyVScHikG'
consumer_secret = '6P0hFmQjRhKrh7uCNXozg4Tx7rVCXQJN5aJb1e4qWRrfY1HO6s'
access_token = '1245212494756372480-JTPEBh7qB935HTfy7jJvwz6AlRIYrA'
access_secret = 'neA4apdl3958t1UHpm6n1venOhBTYnBfnxypn7lqXNOHG'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
import tweepy
from datetime import datetime, timedelta

# Your Twitter API credentials
consumer_key = 'sUc2H25GMIbQJYr85SDQ6KMt6'
consumer_secret = 'q8kIeKbfOcsutkPEaudTHcnikyQD9PH5WwW1ZAPmC4z0NDvZIZ'
access_token = '1408623305884520448-sTKiZCVaLvfArd0vUzQSuWDOpj4lLe'
access_token_secret = 'avav2mop4UKtXDHw4ntoVlhvkrD8rnzEVwgJI3qnplKoZ'

# Authenticate with OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the username (screen name) of the Twitter account
username = 'timesofgaza'

# Calculate the time range for the last 3 hours
end_time = datetime.now()
start_time = end_time - timedelta(hours=3)

# Initialize a counter for tweet count
tweet_count = 0

try:
    # Get tweets from @timesofgaza
    tweets = api.user_timeline(screen_name=username, count=200)

    # Loop through tweets and count those within the specified time range
    for tweet in tweets:
        if start_time <= tweet.created_at <= end_time:
            tweet_count += 1

    print(f"Number of tweets from '@timesofgaza' in the last 3 hours: {tweet_count}")

except tweepy.TweepError as e:
    print(f"Tweepy Error: {e}")
except Exception as ex:
    print(f"Error: {ex}")

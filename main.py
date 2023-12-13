import tweepy
from datetime import datetime, timedelta
from alpaca.trading.client import TradingClient

consumer_key = 'QHN6E3mGT2m9X0pizLQ4HNBU3'
consumer_secret = 'JLu9Y7xcVxuqidHDn88YjTScClTI2HXKn2dwcGob8G7WBk90uc'
access_token = '1408623305884520448-WYQXDwCxdnqV74bymXop938dd9W9ur'
access_token_secret = 'sRpHroL9a8DkcLebrk0chDz6bX8VHZ2XNzmH0Pr4kw2oc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)




    # Get tweets from @timesofgaza
account = 'timesofgaza'
tweets = api.user_timeline(screen_name=account, count=3)

print (tweets)



"""alpaca_api_key = 'PKZ9FFDTB1MJGB2J8BT3'
alpaca_secret_key = 'KOP9jOMhyfwrs5dKlPrD9yM9knBbkmfldW8kVK1O'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


alpaca = TradingClient(api_key=alpaca_api_key, secret_key=alpaca_secret_key)


tweet_actions = {
    (0, 5): 10,
    (5, 10): 3,
    (10, 15): -5,
    (15, float('inf')): -10
}




def track_tweet_count(screen_name, timeframe_hours):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=timeframe_hours)


    tweets = tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode='extended').items()

    tweet_count = sum(
        1 for tweet in tweets
        if start_time <= tweet.created_at <= end_time
    )
    
    return tweet_count

try:

    tweet_count = track_tweet_count('timesofgaza', 3)
    print(f"Number of tweets from '@timesofgaza' in the last 3 hours: {tweet_count}")


except Exception as e:
    print(f"Error: {e}")

 
    for (min_count, max_count), stock_action in tweet_actions.items():
        if min_count <= tweet_count < max_count:
            if stock_action > 0:
 
                alpaca.submit_order(
                    symbol='LMT',  
                    qty=stock_action,
                    side='buy',
                    type='market',
                    time_in_force='day'
                )
                print(f"Bought {stock_action} shares of Lockheed Martin.")
            elif stock_action < 0:
                
                alpaca.submit_order(
                    symbol='LMT',  
                    qty=abs(stock_action),
                    side='sell',
                    type='market',
                    time_in_force='day'
                )
                print(f"Sold {abs(stock_action)} shares of Lockheed Martin.")
            break
    else:
        print("No action taken based on tweet count.")

except Exception as e:
    print(f"Error: {e}")
"""
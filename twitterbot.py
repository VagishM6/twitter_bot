import tweepy
import time

# API key and secret key from Twitter API
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
# Access token and Secret Token from Twitter API
auth.set_access_token('access_token', 'access_token_secret')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()


# Connect to Twitter API
try:
    api.verify_credentials()
    print("Authentication Successful...")
except:
    print("Authentication Error")


# Screen Name
print('[+] User Detected: ' + user.screen_name + '\n')


# Follower Names
print('Displaying Followers names...')
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)


# follow back using follower names
for follow_back in tweepy.Cursor(api.followers).items():
    # provide user name to follow
    if follow_back.name == 'UserName': 
        follow_back.follow()
        print(f'Followed, {follow_back.name}\n')


# favourite based on keyword
print('Tweet Favouriting in progress...')
favourite_item = 'inhumans'
number_of_favourite = 200
for tweet in tweepy.Cursor(api.search, favourite_item).items(number_of_favourite):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# retweet based on keyword
print('Retweeting in progress...')
retweet_item = 'inhumans'
number_of_retweet = 200
for tweet in tweepy.Cursor(api.search, retweet_item).items(number_of_retweet):
    try:
        print('Tweet Retweeted...')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

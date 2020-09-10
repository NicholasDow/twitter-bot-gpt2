import tweepy
import logging
import os
import dotenv
dotenv.load_dotenv()
# Authentication
# 1st is API key
# 2nd is API secret key
logger = logging.getLogger()
def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    print(consumer_key)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


api = create_api()

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

api.update_status("Test tweet from Tweepy Python")

user = api.get_user("NicholasDow6")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

#api.create_friendship("NicholasDow6")

api.update_profile(description="I like shit memes")

tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

for tweet in api.search(q="Nicholas Dow", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

# This lets you do trends, which could be really cool

trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Nicholas Dow","James Hutchins","Glenn Hutchins"], languages=["en"])

tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()
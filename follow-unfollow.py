import tweepy
import os
import dotenv
import logging
import time
import pickle
import datetime
import calendar

dotenv.load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
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

def check_if_last_day_of_week():
    date = datetime.datetime.today().weekday()
    if date == 3:
        return True
    return False

def unfollow_unfollowers(api, blacklist):
    for following in tweepy.Cursor(api.friends).items():
        if not following in tweepy.Cursor(api.followers).items():
            logger.info(f"Unfollowing {following.name}")
            print(following)
            api.destroy_friendship(following.screen_name)
            blacklist.append(following)
            pickle.dump( blacklist, open( "blacklist.p", "wb" ) )

def follow_followers(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
def main():
    api = create_api()
    while True:
        if not os.path.isfile('./blacklist.p'):
            blacklist = []
            pickle.dump(blacklist, open( "blacklist.p", "wb" ))
        blacklist = pickle.load(open("blacklist.p", "rb" ) )
        follow_followers(api)
        if check_if_last_day_of_week:
            unfollow_unfollowers(api, blacklist)
        logger.info("Waiting...")
        time.sleep(3600)
        

if __name__ == "__main__":
    main()
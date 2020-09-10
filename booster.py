from t-bot import create_api

import tweepy
import logging
from config import create_api
import time
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        blacklist = pickle.load(open("blacklist.p", "rb" ))
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.user.following and not tweet.user in blacklist:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.user.follow()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main():
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["Harvard", "Data Science", "Machine Learning"], languages=["en"])

if __name__ == "__main__":
    main()
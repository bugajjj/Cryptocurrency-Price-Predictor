import tweepy
import os
from dotenv import load_dotenv
import logging

# Create logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Load .env file
load_dotenv()

def post_content(msg):
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_secret = os.getenv('ACCESS_SECRET')

    client_v1 = tweepy.API(tweepy.OAuth1UserHandler(consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_secret))
    client_v2 = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=access_secret)

    try:
        response = client_v2.create_tweet(text=msg)
        logger.info("Tweet posted successfully")
    except Exception as e:
        logger.error("Error posting tweet: %s", str(e))

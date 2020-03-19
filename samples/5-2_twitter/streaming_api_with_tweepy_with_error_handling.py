import os
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
import tweepy

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class Timeout(Exception):
    pass


class StreamListener(tweepy.streaming.StreamListener):

    def on_status(self, status):
        print('@' + status.author.screen_name, status.text)

    def on_error(self, status_code):
        logger.info('Error occurred', status_code)
        super().on_error(status_code)

    def on_timeout(self):
        logger.info('Timeout detected')
        super().on_timeout()

    def on_exception(self, exception):
        logger.error('Exception occurred: {}'.format(exception))


logger.info('Starting Listener')
stream = tweepy.Stream(auth, StreamListener())
stream.sample(languages=['ja'])

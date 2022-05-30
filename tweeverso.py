import tweepy
import time


auth = tweepy.OAuthHandler("acordapedrinho", "quehojetemcampeonato")
auth.set_access_token("pirilimpirilim", "alguemligoupramim")
api = tweepy.API(auth)

api = tweepy.API(auth)

for tweets in tweepy.Cursor(api.search_tweets, q="#BBB", lang="pt", result_type="recent").items(10):
   print(tweets.text)
   tweets.favorite()
   tweets.retweet()
   time.sleep(10)

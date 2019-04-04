from typing import TextIO

import tweepy
import csv
from textblob import TextBlob
consumer_key = 'rDG1RfdbljHKiXWsb2s3WhzoY'
consumer_secret = 'VQbsd4MaDs4jEd84DjBgTxES3uuZSFL6w2EJdD9HQ87QHDYnaH'

access_token = '1111525650907578368-e3dnD7SU94SG6EAsmt99DrvuDvgBh3'
access_token_secret = 'uL8KcSrQRfwOplQb68bq1IuaS2xHGiwYnTiYpHMgBlIWH'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump',count=10)
threshold = 0


with open('csvfile1.csv','w',encoding='utf-8') as file:
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        var = analysis.sentiment.polarity
        if var > threshold:
            file.write(tweet.text + 'POSITIVE' '\n''\n')
        elif var == threshold:
            file.write(tweet.text + 'NEUTRAL' +'\n''\n' )
        else:
            file.write(tweet.text + 'NEGATIVE' '\n''\n')

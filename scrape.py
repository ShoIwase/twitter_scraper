# coding: utf-8
import sys
from bs4 import BeautifulSoup
from datetime import datetime

soup = BeautifulSoup(sys.stdin,"html.parser")
tweets = soup.findAll('li',{"class":'js-stream-item'})

for tweet in tweets:
    if tweet.find('p',{"class":'tweet-text'}):
        tweet_time = datetime.fromtimestamp(int(tweet.find('span', '_timestamp')['data-time']))
        tweet_text = tweet.find('p',{"class":'tweet-text'}).text.encode('utf8').replace("\n", "").replace(",", "")
        
        print tweet_time,
        print ',',
        print tweet_text
    else:
        continue
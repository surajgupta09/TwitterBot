import tweepy
import csv
import pandas as pd
import sys

# API credentials here
consumer_key = 'BVGnYGzai5quIftplXDoyA9uC'
consumer_secret = 'aPCxlaseew1eE3Gn5dIPKeg1wAZDHJNXjEajZuVmd8nr6JcXO7'
access_token = '2900147654-f1TPy8iGWHvIEUmxPCYFJ055g0GnEqOsc1lnT8k'
access_token_secret = 'DWhKpta7V9O2AEI8wvbMg7tAB8bbjIHBmlDlVH3FV3ASE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Search word/hashtag value 
HashValue = ""

# search start date value. the search will start from this date to the current date.
StartDate = ""

# getting the search word/hashtag and date range from user
HashValue = input("Enter the hashtag you want the tweets to be downloaded for: ")
StartDate = input("Enter the start date in this format yyyy-mm-dd: ")

# Open/Create a file to append data
csvFile = open(HashValue+'.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=HashValue,count=20,lang="en",since="2020-01-01", tweet_mode='extended').items():
    print (tweet.created_at, tweet.full_text)
    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])

print ("Scraping finished and saved to "+HashValue+".csv")
#sys.exit()

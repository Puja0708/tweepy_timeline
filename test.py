import urllib, json
import sys
import tweepy
from tweepy import OAuthHandler

def twitter_fetch(screen_name = "BBCNews",maxnumtweets=10):
    # API described at https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline

    consumer_token = 's9dOBBCALs6si3QdUZvfTXGmw' #substitute values from twitter website
    consumer_secret = 'MAeaGRjdWQ0qiJDY9HXZJfZklB2ypqZ2PAcpWvuEU059N7A2CC'
    access_token = '2680121616-YVmOy3xXw2PxklYafZUDd7zuOzClX2nIkp1Cm4B'
    access_secret = '6yD2EMvxix0cNkXO9miAimFcaPEe8OwYfghynf3pBnvBH'
    
    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    api  = tweepy.API(auth)
    
    for status in tweepy.Cursor(api.user_timeline,id=screen_name).items(2): 
        print status.text+'\n'
        

    #for tweet in tweepy.Cursor(api.search, since='2014-09-16', until='2014-09-17').items(5):
    #    print status.entities.get('hashtags')

    mentions = api.mentions_timeline(count=1)
    for mention in mentions:
        print mention.text
        print mention.user.screen_name



  

 #print the timeline  

if __name__ == '__main__':
    username = str(raw_input())
    twitter_fetch(username,10) 


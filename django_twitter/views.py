from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import tweepy
from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter

def timeline(request):
	#return render_to_response('demo.html')
	#return 'timeline'
	#if __name__ == '__main__':
    return render_to_response(twitter_fetch('Puja_0708',100))

def twitter_fetch(screen_name = "BBCNews",maxnumtweets=100):
    # API described at https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline
    response = HttpResponse()

    consumer_token = 's9dOBBCALs6si3QdUZvfTXGmw' #substitute values from twitter website
    consumer_secret = 'MAeaGRjdWQ0qiJDY9HXZJfZklB2ypqZ2PAcpWvuEU059N7A2CC'
    access_token = '2680121616-YVmOy3xXw2PxklYafZUDd7zuOzClX2nIkp1Cm4B'
    access_secret = '6yD2EMvxix0cNkXO9miAimFcaPEe8OwYfghynf3pBnvBH'
    
    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    api  = tweepy.API(auth)
    #print api.me().name
    #api.update_status('Hello -tweepy + oauth!')

    for status in tweepy.Cursor(api.user_timeline,id=screen_name).items(2): 
        #return status.text+'\n'
        response.write(status.text)
    return response

def home(request):
    return HttpResponse('''
        Login with <a href=" ">Twitter</a>.<br />
        <form name="myform" action="timeline">
            <input type="text" name="Puja_0708" id="Puja_0708" value="Puja_0708" />
            <input type="submit" value="submit">
        </form>
    ''')


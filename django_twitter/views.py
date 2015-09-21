from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import tweepy
from datetime import datetime
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from django_twitter.forms import ContactForm
from django_twitter.models import Comments
#using django template
from django.template import Template, Context

#using the django forms to access, use localhost:portnumber/handle
def handle_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})

def search_form(request):
    return render(request, 'index.html')

@csrf_exempt
def search(request):
    if request.method == 'POST':
        username = request.POST
    elif request.method == 'GET':
        username = request.GET
    username = str(username)
    #print username
    return twitter_fetch(username, 100)
    #return render_to_response(twitter_fetch(username,100))


    #return render_to_response(twitter_fetch('Puja_0708',100))
#@render_to('django_twitter:timeline.html')
@csrf_exempt
def twitter_fetch(request,maxnumtweets=100):

    response = HttpResponse()

    #getting the given twitter handle out of the django query dict created
    queryDict = QueryDict()
    queryDict = request
    qu = str(queryDict)
    a = qu.split(':')
    b = a[2].split("'")
    handle = b[1]
    # API described at https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline
    
    #print request.urlencode()
    #myDict = dict(queryDict.iterlists())
    #print myDict
    user = str(request)
    #print user
    consumer_token = 's9dOBBCALs6si3QdUZvfTXGmw' #substitute values from twitter website
    consumer_secret = 'MAeaGRjdWQ0qiJDY9HXZJfZklB2ypqZ2PAcpWvuEU059N7A2CC'
    access_token = '2680121616-YVmOy3xXw2PxklYafZUDd7zuOzClX2nIkp1Cm4B'
    access_secret = '6yD2EMvxix0cNkXO9miAimFcaPEe8OwYfghynf3pBnvBH'
    
    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    api  = tweepy.API(auth)

    response.write('<b><u>Tweets : </u></b><br />')
    for status in tweepy.Cursor(api.user_timeline,id=handle).items(100): 
        html = []
        f = []

        #writing user id and tweets in the table(database)
        p1 = Comments(user_id=handle,
                      comment=status.text)
        p1.save()

        #using django template
        t = Template(" {{ name }} ")
        c = Context({'name': status.text})
        f.append(t.render(c))

    l = len(f)
    for i in range(l):
        #html = "<html><body> %s.</body></html>" % f[i]
        return print_tweets(f[i])

        #html.append("<html><body>It is now %s.</body></html>" % f)
        #j = j+1
    #return HttpResponse(html)
        #l = len(html)
    #for i in range(l):
        #return HttpResponse(html[i])
        #<p>Dear {{ handle }},</p>
        #<p>Here is a glimpse of your timeline :</p>
        #<ul>
        #{% for status in tweepy.Cursor(api.user_timeline,id=handle).items(100): %}
         #   <li>{{ status.text }}</li>
        #{% endfor %}
        #</ul>

        #response.write(t)
        #print t
        #return status.text+'\n'
        #response.write(status.text + '<br /> <br />')
        
    #return response

def home(request):

    return HttpResponse('''
        Login with <a href=" ">Twitter</a>.<br />
        <form name="myform" action="search" method="POST">
            <input type="text" name="q" id="q"/>
            <input type="submit" value="submit">
        </form>
    ''')

def print_tweets(request):
    html = "<html><body> %s.</body></html>" % request
    return HttpResponse(html)
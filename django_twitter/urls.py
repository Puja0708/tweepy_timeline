from django.conf.urls import include, url
from django.contrib import admin
from django_twitter.views import timeline, twitter_fetch
from django_twitter.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_twitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^timeline', timeline),
    url(r'^twitter_fetch', twitter_fetch),
]

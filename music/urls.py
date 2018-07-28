from django.conf.urls import url
from . import views
 
app_name = 'myusic'

urlpatterns = [
    #/music homepage
    url(r'^$', views.index,name='index'),

    url(r'^register/^$', views.index,name='register'),

    # /music/question_id
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/question_id/score
    url(r'^(?P<question_id>[0-9]+)/score$', views.detail, name='score'),
]

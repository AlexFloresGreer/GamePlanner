from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
    url(r'^gamelanding$', views.gamelanding, name='gamelanding'),
    url(r'^join$', views.join, name='join'),
    url(r'^start$', views.start, name='start'),
    url(r'^create$', views.create),
    url(r'^gameinfo$', views.gameinfo),

]

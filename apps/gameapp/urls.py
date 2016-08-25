from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
    url(r'^landing$', views.landing, name='landing'),
    url(r'^join$', views.join, name='join'),
    url(r'^start$', views.start, name='start'),
    url(r'^start_game$', views.start_game),
    url(r'^info$', views.info, name="info"),

]

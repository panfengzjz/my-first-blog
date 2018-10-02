from django.conf.urls import url
from . import views
#from django.urls import path, include

urlpatterns = [
    url('^$', views.post_list, name='post_list'), 
]
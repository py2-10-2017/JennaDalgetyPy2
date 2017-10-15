from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'session_words$', views.index),
    url(r'^choices$', views.choices),
    url(r'^clear$', views.clear)
]
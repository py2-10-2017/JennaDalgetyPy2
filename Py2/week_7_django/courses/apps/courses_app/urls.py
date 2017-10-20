from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/create$', views.create),
    url(r'^courses/destroy/(?P<id>\d$)', views.confirm_delete),
    url(r'^courses/delete/(?P<id>\d$)', views.destroy)
]
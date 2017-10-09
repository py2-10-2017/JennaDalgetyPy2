from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'users/new/$', views.new_user),
    url(r'users/$', views.users)
]
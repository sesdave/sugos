from django.conf.urls import url
#from django.urls import path
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    #url(r'^home/$', views.HomeView.as_view(), name="home"),

]
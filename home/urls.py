from django.conf.urls import url
#from django.urls import path
from . import views

urlpatterns = [
    url(r'^home/$', views.HomeView.as_view(), name="home"),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^view_message/$', views.MessageView.as_view(), name="view_message"),

]
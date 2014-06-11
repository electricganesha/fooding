from django.conf.urls.defaults import *
#from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'food.views.indexview', name='index'),
    url(r'^insertview/$', 'food.views.insertview', name='insertview'),
	url(r'^register/$', 'food.views.registerNewUser', name='register'),
	url(r'^createEvent/$', 'food.views.createEvent', name='createEvent'),
    url(r'^reviewEvent/(?P<event_id>[\d]+)$', 'food.views.reviewEvent', name='reviewEvent'),
    url(r'^viewEvent/(?P<event_id>[\d]+)$', 'food.views.viewEvent', name='viewEvent'),
    url(r'^viewUserProfile/(?P<user_id>[\d]+)$', 'food.views.viewUserProfile', name='viewUserProfile'),
    url(r'^searchEvents/$', 'food.views.searchEvents', name='searchEvents'),
    url(r'^participateInEvents/(?P<event_id>[\d]+)$', 'food.views.participateInEvents', name='participateInEvents'),
	url(r'^approveRequest/(?P<notification_id>[\d]+)$', 'food.views.approveRequest', name='approveRequest'),
	url(r'^deleteEvent/(?P<event_id>[\d]+)$', 'food.views.deleteEvent', name='deleteEvent'),
	url(r'^deleteNotification/(?P<notification_id>[\d]+)$', 'food.views.deleteNotification', name='deleteNotification'),
    url(r'^success/$', 'food.views.success', name='success'),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/remote/users/cmarques/dev/fooding/staticfiles/'}),
	(r'^login/$', 'food.views.login_user'),
	(r'^ajaxMapRefresh/$', 'food.views.ajaxMapRefresh'),
	(r'^logout/$', 'food.views.logout_user'),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^viewNotifications/$', 'food.views.viewNotifications', name='viewNotifications'),
)
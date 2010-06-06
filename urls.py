from django.contrib import admin

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('misc.orlpro.subscriber.views',
	url(r'^subscribe/$',	'subscribe',	name="subscribe"),
	url(r'^unsubscribe/$',	'unsubscribe',	name="unsubscribe"),	
)

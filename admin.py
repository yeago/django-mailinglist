from django.contrib import admin
from misc.orlpro.subscriber.models import *

class SubscriberAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subscriber,SubscriberAdmin)

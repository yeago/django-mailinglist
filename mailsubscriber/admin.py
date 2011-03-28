from django.contrib import admin
from mailsubscriber.models import Subscriber 

class SubscriberAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subscriber,SubscriberAdmin)

from django import forms
from django.template import loader, Context
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.mail import send_mail

from mailsubscriber.models import Subscriber

class SubscribeForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		fields = ['email']
	def save(self,*args,**kwargs):
		current_site = Site.objects.get_current()
		site_name = current_site.name
		domain = current_site.domain
		model = Subscriber.objects.create(email=self.cleaned_data['email'])

		t = loader.get_template("subscriber/verification_email.txt")
		c = {
			'email': model.email,
			'owner': getattr(settings,"MAILING_LIST_OWNER","Yeago"),
			'title': getattr(settings,"MAILING_LIST_OWNER_TITLE","Ninja"),
			'domain': domain,
			'site_name': site_name,
			'token': model.get_token()
		}
		send_mail("[%s] - Verify subscription" % site_name,
			t.render(Context(c)), None, [model.email])
		return model

	def clean_email(self):
		if 'email' in self.cleaned_data and self.cleaned_data['email']:
			if Subscriber.objects.filter(email=self.cleaned_data['email'],verified=True):
				raise forms.ValidationError("This address is already subscribed.")
			if Subscriber.objects.filter(email=self.cleaned_data['email'],verified=False):
				raise forms.ValidationError("A verification email has already been sent. Please check your spam-box if you haven't received it")
			return self.cleaned_data['email']

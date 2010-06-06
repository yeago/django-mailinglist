from django.db import models
from datetime import datetime
from django.utils.http import int_to_base36, base36_to_int

class Subscriber(models.Model):
	date_added = models.DateTimeField()
	email = models.EmailField()
	verified = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if not self.date_added:
			self.date_added = datetime.now()
		super(Subscriber, self).save(*args, **kwargs)

	def get_token(self):
		return int_to_base36(self.id * 94)

	def __unicode__(self):
		return '%s' % self.email

def decrypt_token(token):
	return base36_to_int(token) / 94

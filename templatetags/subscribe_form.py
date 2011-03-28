from django.template import Library, Node
from mailsubscriber.forms import SubscribeForm

register = Library()

@register.inclusion_tag('subscriber/subscribe_form.html',takes_context=True)
def subscribe_form(context):
	form = SubscribeForm() 
	if 'request' in context and context['request'].POST:
		form = SubscribeForm(context['request'].POST)
		if form.is_valid():
			form.save()
	return {'form':form, 'context': context}

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import mail_managers
from django.contrib import messages

from mailsubscriber.models import Subscriber, decrypt_token


def subscribe(request):
    try:
        model = get_object_or_404(Subscriber,email=request.GET['email'],pk=decrypt_token(request.GET['token']),verified=False)
        model.verified = True
        model.save()
        mail_managers("New mailing-list subscriber - %s" % request.GET['email'],"Subject says it all.")
        messages.success(request,"Your email address has been confirmed. Welcome!")
        return redirect("/")
    except:
        raise Http404

def unsubscribe(request):
    model = get_object_or_404(Subscriber,email=request.GET['email'],pk=decrypt_token(request.GET['token']))
    model.delete()
    mail_managers("Mailing-list unsubscriber - %s" % request.GET['email'],"Subject says it all.")
    return HttpResponse("Your email address has been removed from the list. So long!")

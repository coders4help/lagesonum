from twilio import twiml

from django.views.generic import View
from django.utils.decorators import method_decorator

from django_twilio.decorators import twilio_view


class SMSNotificationView(View):

    @method_decorator(twilio_view)
    def dispatch(self, request, *args, **kwargs):
        return super(SMSNotificationView, self).dispatch(request, *args, **kwargs)

    def post(self, request, message):
        r = twiml.Response()
        r.message(message)
        return r

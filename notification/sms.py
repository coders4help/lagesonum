from twilio import twiml

from django.views.generic import View
from django.utils.decorators import method_decorator

from django_twilio.decorators import twilio_view
from django_twilio.views import message as MessageView
from django_twilio.client import twilio_client

from django.conf import settings


class SMSNotificationView(View):

    @method_decorator(twilio_view)
    def dispatch(self, request, *args, **kwargs):
        return super(SMSNotificationView, self).dispatch(request, *args, **kwargs)

    def send(self, recipient_number, message):
        "sends a message to a number"
        print('sending message "{}" to {} from {}'.format(message, recipient_number, settings.TWILIO_DEFAULT_SENDER))
        twilio_client.sms.messages.create(body=message, to=recipient_number, from_=settings.TWILIO_DEFAULT_SENDER)

    def receive(self, message):
        r = twiml.Response()
        r.message(message)
        return r

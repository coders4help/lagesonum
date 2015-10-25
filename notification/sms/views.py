import logging
from datetime import datetime

from twilio import twiml

from django.views.generic import View
from django.utils.decorators import method_decorator

from django_twilio.request import decompose
from django_twilio.decorators import twilio_view
from django_twilio.client import twilio_client

from django.conf import settings

from website.models import Subscription, Place

logger = logging.getLogger(__name__)


class SMSNotificationView(View):
    http_method_names = ['post']

    @method_decorator(twilio_view)
    def dispatch(self, request, *args, **kwargs):
        return super(SMSNotificationView, self).dispatch(request, *args, **kwargs)

    def send(self, recipient_number, message):
        "sends a message to a number, uses the twilio client directly instead of twiml response"
        logger.info('sending message "{}" to {} from {}'.format(
            message, recipient_number, settings.TWILIO_DEFAULT_SENDER)
        )
        twilio_client.sms.messages.create(body=message, to=recipient_number, from_=settings.TWILIO_DEFAULT_SENDER)

    def post(self, request):

        # parse twilio request
        twilio_request = decompose(request)
        message = twilio_request.body
        from_number = twilio_request.from_
        logger.info('sms from {}: {}'.format(from_number, message))

        r = twiml.Response()

        # parse message body
        if message.upper() is 'STOP':
            subscription = Subscription.objects.get(number=from_number)
            subscription.cancelled = datetime.now()
            subscription.save()
            logger.info('unsubscribed', subscription)

            r.message('You have been unsubscribed')

        if message.upper().startswith('CONFIRM'):
            # TODO check confirmation hash
            subscription = Subscription.objects.get(number=from_number)
            subscription.phone_confirmed = True
            subscription.save()

        else:
            logger.info('sms: invalid command', message)
        return r

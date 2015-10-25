from datetime import datetime

from django.views.generic import View

from website.models import Number, Subscription

from notification.sms import SMSNotificationView
# from notification.email import EmailNotificationView


class BaseNotificationView(View):
    "Generic notification view, to dispatch to separate"

    def send(instance, **kwargs):
        pass


class ConfirmationView(BaseNotificationView):

    def send(instance, **kwargs):
        pass


class NumberUpdatedView(BaseNotificationView):

    def send(instance, **kwargs):
        subscribers = Subscription.objects.filter(number=instance.number, cancelled__isnull=True)

        for s in subscribers:
            # if s.email_confirmed:
            #    EmailNotificationView.send(instance.)
            if s.phone_confirmed:
                message = '{} updated'.format(instance.number)
                SMSNotificationView.send(instance, s.phone.as_e164, message)

            s.last_notify = datetime.now()
            s.save()

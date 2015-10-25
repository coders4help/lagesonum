from datetime import datetime

from django.views.generic import View
from django.utils.translation import ugettext_lazy as _

from website.models import Number, Subscription

from notification.sms.views import SMSNotificationView
from notification.email.views import EmailNotificationView
from notification.telegram.views import TelegramNotificationView


class BaseNotificationView(View):
    "Generic notification view"

    def send(instance, **kwargs):
        pass


class ConfirmationView(BaseNotificationView):

    def send(instance, **kwargs):
        pass


class NumberUpdatedView(BaseNotificationView):

    def send(instance, **kwargs):
        subscribers = Subscription.objects.filter(number=instance.number, cancelled__isnull=True)

        message = _('LaGeSo number {} updated').format(instance.number)

        for s in subscribers:
            if s.email_confirmed:
                EmailNotificationView.send(instance.email, instance.number)
            if s.phone_confirmed:
                SMSNotificationView.send(instance, s.phone.as_e164, message)
            if s.telegram_confirmed:
                TelegramNotificationView.send(instance, s.telegram, message)

            s.last_notify = datetime.now()
            s.save()

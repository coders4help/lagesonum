from datetime import datetime

from django.views.generic import View
from django.utils.translation import ugettext_lazy as _

from website.models import Subscription

from notification.sms.views import SMSNotificationView, SMSConfirmationView
from notification.email.views import EmailNotificationView, EmailConfirmationView
from notification.telegram.views import TelegramNotificationView


class BaseNotificationView(View):
    "Generic notification view"

    def send(instance, **kwargs):
        pass


class ConfirmationView(BaseNotificationView):

    def send(instance, **kwargs):
        # if instance.email:
        #     EmailConfirmationView.send(instance.email, instance.number)
        # if instance.phone:
        #     SMSConfirmationView.send(instance, s.phone.as_e164)
        # if instance.telegram:
        #     TelegramConfirmationView.send(instance, s.telegram)
        pass


class NumberUpdatedView(BaseNotificationView):

    def send(instance, **kwargs):
        subscribers = Subscription.objects.filter(number=instance.number, cancelled__isnull=True)

        date_updated = datetime.now()
        message = _('Someone reported seeing number {} at LaGeSo at {} on {}.') \
            .format(instance.number, date_updated.strftime('%D'), date_updated.strftime('%H:%M'))

        for s in subscribers:
            if s.email_confirmed:
                EmailNotificationView.send(instance.email, instance.number)
            if s.phone_confirmed:
                message += _('Reply with STOP at any time to cancel this notification.')
                SMSNotificationView.send(instance, s.phone.as_e164, message)
            if s.telegram_confirmed:
                message += _('Reply with STOP at any time to cancel this notification.')
                TelegramNotificationView.send(instance, s.telegram, message)

            s.last_notify = date_updated
            s.save()

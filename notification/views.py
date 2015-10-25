from datetime import datetime

from django.views.generic import View

from notification.sms import SMSNotificationView
# from notification.email import EmailNotificationView


class NotificationView(View):
    "Generic notification view, to dispatch to separate"

    def dispatch(self, request, subscription):
        print('NotificationView', subscription)


class ConfirmSubscriptionView(NotificationView):

    def post(self, subscription):
        pass


class SendNotificationView(NotificationView):

    def post(self, subscription):

        if subscription.cancelled:
            return False

        # if subscription.email_confirmed:
        #    EmailNotificationView.post(subscription.email)
        if subscription.phone_confirmed:
            SMSNotificationView.post('your number is updated')

        subscription.last_notify = datetime.now()

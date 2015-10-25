from django.db.models.signals import post_save
import django.dispatch

from website.models import Number, Subscription

from notification.views import SendNotificationView, SendConfirmationView

confirm_subscription = django.dispatch.Signal()
number_updated = django.dispatch.Signal()

# connect confirmation views
confirm_subscription.connect(SendConfirmationView, sender=Subscription)
post_save.connect(SendConfirmationView, sender=Subscription)

# connect number update views
number_updated.connect(SendNotificationView, sender=Number)
post_save.connect(SendNotificationView, sender=Number)

from django.db.models.signals import post_save
import django.dispatch

from website.models import Number, Subscription

from notification.views import ConfirmationView, NumberUpdatedView

confirm_subscription = django.dispatch.Signal()
number_updated = django.dispatch.Signal()

# connect confirmation views
confirm_subscription.connect(ConfirmationView.send, sender=Subscription)
post_save.connect(ConfirmationView.send, sender=Subscription)

# connect number update views
number_updated.connect(NumberUpdatedView.send, sender=Number)
post_save.connect(NumberUpdatedView.send, sender=Number)

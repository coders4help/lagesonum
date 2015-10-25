from django.views.generic import View
from django.utils.translation import ugettext_lazy as _


class TelegramNotificationView(View):

    def send(self, recipient_address, message):
        # TODO, perform json post as per https://github.com/volunteer-planner/lagesonum/issues/98
        pass

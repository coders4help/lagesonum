import traceback
from django.http import HttpResponse


class PlainExceptionsMiddleware(object):
    def process_exception(self, request, exception):
        # request is coming from twilio, provide plaintext traceback
        if "SmsSid" in request.POST:
            return HttpResponse(traceback.format_exc(exception), content_type="text/plain", status=500)

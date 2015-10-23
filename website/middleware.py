# -*- coding: utf-8 -*-

from django.utils.translation import LANGUAGE_SESSION_KEY
from lagesonum.settings import LANGUAGES


class SessionLocaleMiddleWare(object):

    def process_request(self, request):
        saved_lang = None
        current_lang = request.LANGUAGE_CODE or None

        if hasattr(request, 'session'):
            if LANGUAGE_SESSION_KEY in request.session:
                saved_lang = request.session[LANGUAGE_SESSION_KEY]

            if current_lang and (not saved_lang or current_lang != saved_lang):
                request.session[LANGUAGE_SESSION_KEY] = current_lang

        for lang in LANGUAGES:
            if current_lang == lang[0]:
                setattr(request, 'current_language', lang)
                break

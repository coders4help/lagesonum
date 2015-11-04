# -*- coding: utf-8 -*-

import logging
import datetime
import re

from django import http
from django.conf import settings
from django.core.urlresolvers import reverse, resolve
from django.db.models import Count, Max
from django.shortcuts import render
from django.utils.translation import LANGUAGE_SESSION_KEY, check_for_language

from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormMixin

from .forms import QueryForm
from .models import Number, Place, Holiday

logger = logging.getLogger(__name__)


def set_language(request):
    next_view = request.POST.get('next', request.GET.get('next'))
    lang_code = request.POST.get('lang', request.GET.get('lang'))
    response = http.HttpResponseNotAllowed(['POST', 'GET'])

    if request.method == 'POST' or request.method == 'GET':
        if lang_code and check_for_language(lang_code):
            response = http.HttpResponseRedirect('/{}/?redirect_to={}'.format(lang_code, next_view))
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code,
                                    max_age=settings.LANGUAGE_COOKIE_AGE,
                                    path=settings.LANGUAGE_COOKIE_PATH,
                                    domain=settings.LANGUAGE_COOKIE_DOMAIN)
        else:
            response = http.HttpResponseNotFound()

    return response


class CustomRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # try to get redirect target
        try:
            redir = self.request.GET.get('redirect_to')
            self.url = reverse(redir)

            # remove 'redirect_to' from query string
            query_string = self.request.META.get('QUERY_STRING')
            if query_string:
                query_string = query_string.replace('redirect_to={}'.format(redir), '').replace('^&', '')
                self.request.META.update({'QUERY_STRING': query_string})
        except:
            # if redirect target is not a known view: try path prefixed by lang
            try:
                self.url = reverse(resolve('/en/{}'.format(self.request.get_full_path())))
            except:
                # if we can't get a view from path URL: fall back to default, using 'pattern_name'
                pass

        return super().get_redirect_url(*args, **kwargs)


class QueryView(TemplateView, FormMixin):
    http_method_names = ['get', 'post']
    form_class = QueryForm
    template_name = 'query.html'

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = self.form_class()
        context = super().get_context_data(**kwargs)

        # TODO make variable if multiple locations are served
        context['location'] = Place.objects.get(name='LAGeSo').id

        return context

    def post(self, request, *args, **kwargs):
        response_data = {'result': None, 'notfound': True}

        location = None
        form = self.get_form()
        if form.is_valid():
            location = form.cleaned_data.get('location')
            number=form.cleaned_data.get('number')
            response_data.update(self.query_number(location, number))

        response = None
        response_data.update({'location': location.id if location else 0})

        if not response:
            response_data.update({'form': form})
            response = render(request, self.template_name, dictionary=response_data)

        return response

    def form_valid(self, form):
        try:
            Number.objects.get(number=form.cleaned_data.get('number'))
        except Number.DoesNotExist:
            pass

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('query', args=self.args, kwargs=self.kwargs)

    def query_number(self, location, number):
        result = {'result': number, 'notfound': True}

        try:
            n = Number.objects.filter(location=location, number=number).get()
        except Number.DoesNotExist:
            if re.match(u'(?ai)[A-Z]\d{3}|[A-C][A-Z]\d{2}', number):
                # "normal" not found
                result.update({'notfound': True})
            elif re.match(u'[D-Z][A-Z]\d{2}', number):
                # "special" not found: newer numbers
                result.update({'notfound': True, 'new_process': True})
        else:
            result.update({'notfound': False})
            if not n.appointment:
                n.appointment = self.get_next_appointment(location, n.incomplete)
                n.save(force_update=True)

            result.update({
                'result': n.number,
                'appointment': n.appointment,
                'incomplete': n.incomplete,
                'missed': not n.incomplete,
            })
        return result

    def get_next_appointment(self, location, incomplete):
        query = Number.objects.filter(location=location, incomplete=incomplete, appointment__gt=datetime.date.min)
        maxdate = query.aggregate(maxdate=Max('appointment')).get('maxdate')
        if not maxdate:
            # FIXME Make this 'DAY_ONE' location related
            return location.release_date
            # settings.APP_SETTINGS.get('APPOINTMENTS').get('DAY_ONE')

        count_query = Number.objects.filter(location=location, incomplete=incomplete, appointment=maxdate)\
            .values('appointment').annotate(count=Count('appointment')).order_by('appointment')

        query_result = count_query.get()
        count = query_result.get('count', 0)
        # FIXME Make this 'PER_DAY' location related
        # max_per_day_settings = settings.APP_SETTINGS.get('APPOINTMENTS').get('PER_DAY')
        # if count < max_per_day_settings.get('INCOMPLETE' if incomplete else 'MISSED'):
        per_day = location.per_day_incomplete if incomplete else location.per_day_missed
        if count < per_day:
            return maxdate
        else:
            return self.get_next_working_day(location, maxdate)

    @staticmethod
    def get_next_working_day(location, maxdate):
        for i in range(1, 7):
            next_day = maxdate + datetime.timedelta(i)
            # FIXME Add list of holidays (etc.) to calculation
            if 1 <= next_day.isoweekday() <= 5:
                try:
                    Holiday.objects.get(location=location, date=next_day)
                    continue
                except Holiday.DoesNotExist:
                    return next_day

        return None


class DisplayView(TemplateView):
    template_name = 'display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        oldest_to_be_shown = datetime.datetime.combine(datetime.date.today() -
                                                       datetime.timedelta(
                                                           days=settings.APP_SETTINGS['DISPLAY']['MAX_DAYS']),
                                                           datetime.datetime.min.time())

        verified_numbers = Number.objects.filter(timestamp__gte=oldest_to_be_shown, user__isnull=False)\
            .order_by('-timestamp')\
            .values('number')[:settings.APP_SETTINGS['DISPLAY']['SIZE']]
        logger.debug(u'Verified numbers: {}'.format(len(verified_numbers)))

        numbers = Number.objects.filter(timestamp__gte=oldest_to_be_shown)\
            .values('number')\
            .annotate(count=Count('number'))\
            .filter(count__gte=3)\
            .order_by('number')[:settings.APP_SETTINGS['DISPLAY']['SIZE']]
        logger.debug(u'Numbers: {}'.format(len(numbers)))

        result = {}
        for n in numbers:
            result[n['number']] = n['count']
        for n in verified_numbers:
            result[n['number']] = '∞'

        context['numbers'] = []
        for n in sorted(set(result.keys())):
            context['numbers'].append({'number': n, 'count': result[n]})
        context['min_count'] = 3
        context['since'] = oldest_to_be_shown
        return context

# -*- coding: utf-8 -*-

from django.core.management.commands import makemessages


class Command(makemessages.Command):

    def handle(self, *args, **options):
        options.setdefault('no_wrap', 'True')
        options.setdefault('no_obsolete', 'True')
        options.setdefault('locale', 'en')

        return super().handle(*args, **options)

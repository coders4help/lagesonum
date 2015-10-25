# -*- coding: utf-8 -*-

import sass
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        # TODO: Make (more) dynamic
        outfile = settings.BASE_DIR + '/website/static/css/main.css'
        f = open(outfile, 'w')

        # TODO: Error handling
        infile = settings.BASE_DIR + '/website/scss/main.scss'
        f.write(sass.compile(filename=infile))

        f.close()

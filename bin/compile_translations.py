# -*- conding: utf-8 -*-

import os
import polib
import sys

from sys import stderr

LOCALES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lagesonum/locales'))

if '__main__' == __name__:
    locale_dirs = sys.argv[1:] if 1 < len(sys.argv) else [LOCALES_DIR]

    for locale_dir in locale_dirs:
        if not (os.path.exists(locale_dir) and os.path.isdir(locale_dir)):
            print(u'Locales directory \'{}\' does not exist or is not a directory'.format(locale_dir), file=stderr)
            continue

        i18n_files = []
        for subdir, dirs, files in os.walk(LOCALES_DIR, followlinks=True):
            for file in files:
                if file.endswith('.po'):
                    i18n_files.append({'dir': os.path.relpath(subdir, os.getcwd()), 'file': file})

        for pofile in i18n_files:
            print(u'Processing {}'.format(pofile['dir']))
            pofile_name = os.path.join(pofile.get('dir'), pofile['file'])
            mofile_name = os.path.join(pofile.get('dir'), 'messages.mo')
            polib.pofile(pofile_name).save_as_mofile(mofile_name)
            print(u'Compiled {}'.format(pofile['file']))

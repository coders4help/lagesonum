# -*- coding: utf-8 -*-

from .settings import *

DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

SECRET_KEY = 'ThisIsOnlyADevelopmentAndNotSoSecretKey'

INSTALLED_APPS += (
    'debug_toolbar',
)

LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'formatters': {
        'brief': {
            'format': '%(message)s',
        },
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s - %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '../local.log'),
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'WARNING',
        },
        'django': {
            'level': 'WARNING',
            'propagate': True,
        },
        'django.request': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.sql': {
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'INFO',
            'propagate': True,
        },
        'website': {
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

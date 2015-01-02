# -*- coding: utf-8 -*-

# python import
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY_MINER', 'Development')
    WTF_CSRF_ENABLED = True

    FLASKY_MAIL_SUBJECT_PREFIX = '[Hamid FzM]'
    FLASKY_MAIL_SENDER = 'Hamid FzM <mail@hamidfzm.ir>'
    FLASKY_ADMIN = 'Hamid FzM'

    LANGUAGES = {
        'en': 'English',
        'fa': u'فارسی'
    }

    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'UTC+03:30'

    MONGODB_SETTINGS = {'DB': 'miner',
                        'HOST': '127.0.0.1',
                        'PORT': 27017}

    INSTALLED_BLUEPRINTS = ['main',
                            'user']

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class DeploymentConfig(Config):
    DEBUG = False
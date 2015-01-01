__author__ = 'hamid'

__all__ = ['db']

from flask.ext.mongoengine import MongoEngine

db = MongoEngine()
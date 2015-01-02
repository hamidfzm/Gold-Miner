__author__ = 'hamid'

__all__ = ['db']

from flask.ext.mongoengine import MongoEngine
from flask.ext.httpauth import HTTPBasicAuth

db = MongoEngine()
auth = HTTPBasicAuth()
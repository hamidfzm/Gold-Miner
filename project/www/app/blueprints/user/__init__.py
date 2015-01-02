__author__ = 'hamid'

from flask import Blueprint

mod = Blueprint('user', __name__, url_prefix='/user')

from . import views
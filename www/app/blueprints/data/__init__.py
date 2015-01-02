__author__ = 'hamid'

from flask import Blueprint

mod = Blueprint('data', __name__, url_prefix='/')

from app.blueprints.data import views
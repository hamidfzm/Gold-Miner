__author__ = 'hamid'

from flask import Blueprint

mod = Blueprint('main', __name__, url_prefix='/')

from app.blueprints.main import views

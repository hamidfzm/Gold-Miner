__author__ = 'hamid'

from flask import Blueprint

mod = Blueprint('data', __name__, url_prefix='/data')

from app.blueprints.data import views
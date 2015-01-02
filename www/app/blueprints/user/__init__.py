__author__ = 'hamid'

from flask import Blueprint

mod = Blueprint('user', __name__, url_prefix='/user')

from app.blueprints.user import views
# -*- coding: utf-8 -*-
__author__ = 'hamid'

# python imports
from mongoengine import DoesNotExist

# flask imports
from flask import request, jsonify, g

# project imports
from . import mod
from app.blueprints.user.models import User
from app.blueprints.user.forms import Login


@mod.route('/api/v1/', methods=['POST'])
def authenticate():
    json = Login.from_json(request.json, csrf_enabled=False)

    if json.validate():
        try:
            user = User.objects.get(username=json.username.data)
            if user.verify_password(json.password.data):
                return jsonify(token=user.generate_token())
            else:
                return jsonify(), 401
        except DoesNotExist:
            pass
    return jsonify(errors=json.errors), 406


@mod.route('/api/v1/', methods=['GET'])
@User.auth
def view():
    return jsonify(username=g.user.username,
                   name=g.user.name)
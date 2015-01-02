__author__ = 'hamid'

# python imports
from mongoengine.connection import get_connection

# flask imports
from flask import jsonify
from bson.json_util import _json_convert

# project imports
from . import mod


@mod.route('/api/v1/tgju/', methods=['GET'])
def get():
    db = get_connection()['tgju']
    data = dict()
    for collection in db.collection_names():
        if collection == 'system.indexes':
            continue
        data[collection] = _json_convert(db[collection].find())

    return jsonify(**data)
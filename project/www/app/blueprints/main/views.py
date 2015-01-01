# -*- coding: utf-8 -*-
__author__ = 'hamid'

# project import
from . import mod


@mod.route('/')
def index():
    return 'hello'
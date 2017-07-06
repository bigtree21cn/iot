# encoding: utf-8
"""
auth module
============
"""
from .resources import authAPI


def init_app(app):
    from app.extensions import api
    api.add_resource(authAPI, '/api/users/', endpoint='users')
# encoding: utf-8
"""
auth module
============
"""
from .resources import UserAPI, TokenAPI


def init_app(app):
    from app.extensions import api
    api.add_resource(UserAPI, '/api/users/', endpoint='users')
    api.add_resource(TokenAPI, '/api/login/', endpoint='token')
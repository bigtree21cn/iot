# encoding: utf-8
# pylint: disable=invalid-name,wrong-import-position
"""
Extensions setup
================
Extensions provide access to common resources of the application.
Please, put new extension instantiations and initializations here.
"""


from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy(session_options={'autocommit': True})
api = Api()
auth = HTTPBasicAuth()


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            db,
            api,
    ):
        extension.init_app(app)
        extension.app = app


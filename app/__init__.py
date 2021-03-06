# encoding: utf-8
"""
RESTful API Server.
"""
import logging
import os
import sys
from flask import Flask
from logging.handlers import RotatingFileHandler
from logging import Formatter
from flask_cors import CORS

'''
from functools import wraps
from flask import (
    Flask,
    current_app,
    jsonify,
    request,
)

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except BadRequest, e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, current_app.config[schema_name])
            except ValidationError, e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator
'''

class Serializer(object):
    __public__ = None
    "Must be implemented by implementors"

    def to_serializable_dict(self):
        dict = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            if value:
                dict[public_key] = value
        return dict


CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
    'production': 'config.ProductionConfig',
    'local': 'local_config.LocalConfig',
}




def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    app = Flask(__name__, **kwargs)
    CORS(app)

    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if not env_flask_config_name and flask_config_name is None:
        flask_config_name = 'local'
    elif flask_config_name is None:
        flask_config_name = env_flask_config_name
    else:
        if env_flask_config_name:
            assert env_flask_config_name == flask_config_name, (
                "FLASK_CONFIG environment variable (\"%s\") and flask_config_name argument "
                "(\"%s\") are both set and are not the same." % (
                    env_flask_config_name,
                    flask_config_name
                )
            )

    try:
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])
    except ImportError:
        if flask_config_name == 'local':
            app.logger.error(
                "You have to have `local_config.py` or `local_config/__init__.py` in order to use "
                "the default 'local' Flask Config. Alternatively, you may set `FLASK_CONFIG` "
                "environment variable to one of the following options: development, production, "
                "testing."
            )
            sys.exit(1)
        raise

    log_file_handler = RotatingFileHandler('iot.log')
    log_file_handler.setFormatter(Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'))
    log_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(log_file_handler)

    if app.debug:
        app.logger.setLevel(logging.DEBUG)


    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    app.logger.debug('application initializing done')

    return app
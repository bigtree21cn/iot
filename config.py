# pylint: disable=too-few-public-methods,invalid-name,missing-docstring
import os


class BaseConfig(object):
    SECRET_KEY = 'this is,a.ito;restful/service!'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # POSTGRESQL
    # DB_USER = 'user'
    # DB_PASSWORD = 'password'
    # DB_NAME = 'restplusdb'
    # DB_HOST = 'localhost'
    # DB_PORT = 5432
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
    #     user=DB_USER,
    #     password=DB_PASSWORD,
    #     host=DB_HOST,
    #     port=DB_PORT,
    #     name=DB_NAME,
    # )

    # SQLITE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "example.db"))

    DEBUG = True
    ERROR_404_HELP = False

    ENABLED_MODULES = (
        'auth',
        'measurement',
    )

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('CLOUDSML_API_SERVER_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///db.sqlite'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///dev.sqlite'
#        'mysql+pymysql://root:123456@10.140.1.17/iot?charset=utf8'

class TestingConfig(BaseConfig):
    TESTING = True

    # Use in-memory SQLite database for testing
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///test.sqlite'
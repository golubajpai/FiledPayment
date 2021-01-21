"""Flask configuration."""
from os import environ, path




class BaseConfig:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    


class ProdConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_URI')


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_URI')
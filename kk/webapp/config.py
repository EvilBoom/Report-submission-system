class Config(object):
    SECRET_KEY = 'b05f6a8cccff8805f1277c865f9139f5'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tt:123456@localhost:5432/flask'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tt:123456@localhost:5432/flask'

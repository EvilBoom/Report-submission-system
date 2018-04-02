class Config(object):
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tt:123456@localhost:5432/flask'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tt:123456@localhost:5432/flask'

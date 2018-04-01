class Config(object):
    pass


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://tt:123456@localhost:5432/flask"    

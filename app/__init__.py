from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from config import config
from app.models import db

bootstrap = Bootstrap() 
moment = Moment()
mail = Mail()

def create_app(DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config[DevelopmentConfig])
    config[DevelopmentConfig].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


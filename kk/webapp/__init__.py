from flask import Flask,  redirect, url_for

from .models import db
from .controllers.blog import rss_blueprint

def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)


    @app.route('/')
    def index():
        return redirect(url_for('rss.home'))


    app.register_blueprint(rss_blueprint)

    return app

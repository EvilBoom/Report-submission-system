from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usr/<name>')
def user(name):
    return render_template('use.html',name=name)


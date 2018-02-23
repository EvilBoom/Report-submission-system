from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usr/<name>')
def user(name):
    return render_template('use.html',name=name)


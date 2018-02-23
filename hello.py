from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello word</h1>'

@app.route('/usr/<name>')
def user(name):
    return '<h1>hello %s!</h1>'%name

if __name__ == '__main__':
    app.run(debug=True)

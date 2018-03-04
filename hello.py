from flask import Flask,render_template,session,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_moment import  Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY']= 'Torpedo'

bootstrap = Bootstrap(app) 
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validators_on_submit():
        session['name'] = form.naem.data
        return redirect(url_for('index'))
    return render_template('index.html',form = form ,name = session.get('name'))


@app.route('/usr/<name>')
def user(name):
    return render_template('use.html',name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.error_handlers(500)
def internal_server_error(e):
    return render_template('500.html'),500

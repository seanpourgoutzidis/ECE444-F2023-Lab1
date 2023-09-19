from flask import Flask, render_template, session, redirect, url_for
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from datetime import datetime
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wowzers'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form.html', form = form, name = name)
    


#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask import session
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'JKH98vd8vd??dfdf>><&*4fd'

@app.route('/',methods=['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('form.html', form=form, name=name)

if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
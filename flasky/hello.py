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
from datetime import datetime

class BizError(RuntimeError):
	def __init__(self,code,message):
		self.code = code
		self.message = message

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'JKH98vd8vd??dfdf>><&*4fd'

@app.errorhandler(404)
def page_not_found(e):
	response = make_response('{"__errcode": 3,"__errmsg": "404"}')
	response.headers['Content-Type'] = 'application/json'
	return response

@app.errorhandler(500)
def internal_server_error(e):
	print('internal_server_error')
	response = make_response('{"__errcode": 3,"__errmsg": "500"}')
	if (isinstance(e,BizError)):
		response = make_response('{"__errcode": %d,"__errmsg": "%s"}' % (e.code,e.message))
	response.headers['Content-Type'] = 'application/json;charset=UTF-8'
	return response

@app.route('/create_session')
def create_session():
	session['name'] = 'session_哈哈哈'
	return render_template('index.html')

@app.route('/show_session')
def show_session():
	return render_template('index.html',session_name=session['name'])

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	#return '<p>Your browser is %s</p>' % user_agent, 400

	# response = make_response('<p>Your browser is %s</p>' % user_agent)
	# response.set_cookie('answer', '42')
	# return response

	#return redirect('/user/sdsdsd')
	#abort(404)
	return render_template('index.html')


@app.route('/index2')
def index2():
	return render_template('index.html', current_time=datetime.utcnow())

@app.route('/custom_error')
def custom_error():
	raise BizError(1,'参数错误')

@app.route('/user/<name>')
def user(name):
	#return '<h1>Hello,%s</h1>' % name
	return render_template('USER.html',name=name)

if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
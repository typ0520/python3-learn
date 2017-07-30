#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_script import Manager
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com' 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = '752554930'
app.config['MAIL_PASSWORD'] = 'typ5669298'

mail = Mail(app)
manager = Manager(app)
# app.config.update(MAIL_SERVER='smtp.qq.com',
# 	MAIL_PORT=465,
# 	MAIL_USE_SSL=True,
# 	MAIL_USE_TLS = False,
# 	MAIL_USERNAME = '752554930',
# 	MAIL_PASSWORD = 'typ5669298')

@app.route('/')
def sendmail():
	msg=Message('Hi',sender='752554930@qq.com',recipients=['php12345@163.com'])
	msg.html='<b>hello web</b>'
	print('hahha')
	mail.send(msg)
	print('hahha22')
	return '<h1>ok!</h1>'

if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()

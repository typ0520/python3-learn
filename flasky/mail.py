#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_script import Manager
from flask_mail import Mail,Message

app = Flask(__name__)
manager = Manager(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.163.com' 
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') 
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


@app.route('/')
def index():
	print('mail.user: ' + os.environ.get('MAIL_USERNAME'))
	print('mail.pwd: ' + os.environ.get('MAIL_PASSWORD'))
	msg = Message('test subject',sender=app.config['MAIL_USERNAME'], recipients=['752554930@qq.com']) 
	msg.body = 'test body'
	msg.html = 'test html'
	mail.send(msg)

if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()

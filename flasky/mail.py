#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_script import Manager
from flask_mail import Mail

app = Flask(__name__)
manager = Manager(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.163.com' 
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') 
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()

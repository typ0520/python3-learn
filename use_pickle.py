#!/usr/bin/python3

import pickle


def w():
	d = dict(name='typ0520',age=20)
	#d = {'name':'typ0520','age':20}
	f = open('/Users/tong/Desktop/pickle','wb')
	pickle.dump(d,f)
	f.close()

def r():
	f = open('/Users/tong/Desktop/pickle','rb')
	d = pickle.load(f)
	f.close()
	print(d)

w()
r()
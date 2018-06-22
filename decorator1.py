#!/usr/bin/env python3

def foo():
	print('i am foo')

def user_logging(func):
	print("%s is running" % func.__name__)
	func()

user_logging(foo)



def user_logging2(func):
	def wrapper():
		print("%s is running" % func.__name__)
		func()
	return wrapper

foo = user_logging2(foo)
foo()

@user_logging2
def foo2():
	print('i am foo')

foo2()

def user_logging3(func):
	print('user_logging3')
	def wrapper(name):
		print("%s is running" % func.__name__)
		func(name)
	return wrapper

@user_logging3
def foo3(name):
	print('i am %s' % name)

foo3('typ0520')



def user_logging4(func):
	print('user_logging4')
	def wrapper(*args):
		print("%s is running" % func.__name__)
		func(*args)
	return wrapper

@user_logging4
def foo4(name):
	print('i am %s' % name)

foo4('typ0520')



def user_logging5(func):
	print('user_logging5')
	def wrapper(*args, **kwargs):
		print("%s is running" % func.__name__)
		return func(*args,**kwargs)
	return wrapper

@user_logging5
def foo5(name, age=None, height=None):
	print('i am %s,args=%d,hieght=%d' % (name,age,height))

foo5('typ0520',age=100,height=200)











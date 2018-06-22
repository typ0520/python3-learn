#!/usr/bin/env python3


def user_logging(level):
	print('user_logging: level %s' % level)

	def decorator(func):
		print('decorator: level %s' % level)

		def wrapper(*args, **kwargs):
			print("%s is running, level:%s" % (func.__name__, level))
			return func(*args, **kwargs)
		return wrapper
	return decorator


@user_logging(level="warn")
def foo(name, age=None, height=None):
	print('i am %s,args=%d,hieght=%d' % (name, age, height))


foo('typ0520', age=100, height=200)


class Foo(object):
	def __init__(self, func):
		self._func = func

	def __call__(self):
		print('class decorator runing')
		self._func()
		print('class decorator ending')


@Foo
def bar():
	print('bar')


bar()


# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
    	# 输出 'with_logging',丢失了函数元信息，真正的函数名叫f
    	print('func.__name__ %s' % func.__name__)
    	print(func.__doc__)
    	return func(*args, **kwargs)
    return with_logging


from functools import wraps


def logged2(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		print('func.__name__ %s' % func.__name__)
		print('func.__doc__ %s' % func.__doc__)
		return func(*args, **kwargs)
	return with_logging

# 函数


@logged
def f(x):
   """does some math"""
   return x + x * x


f(100)


@logged2
def test_f(x):
	return x + x * x


test_f(200)

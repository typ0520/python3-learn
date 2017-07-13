#!/usr/bin/python3


class StudentMetaclass(type):
	def __new__(cls,name,bases,attrs):
		print(cls)
		print(name)
		print(bases)
		print(attrs)

		attrs['__tttt__'] = '哈哈哈'
		return type.__new__(cls,name,bases,attrs)

class Student(object,metaclass=StudentMetaclass):
	__sname__ = 'haha'
	def __init__(self,name):
		self.name = name

s = Student('typ0520')

print(s.__tttt__)
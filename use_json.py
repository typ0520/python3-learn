#!/usr/bin/python3

import json


def jsontest():
	d = dict(name='Bob',age=20,score=88)
	json.dumps(d)

	json_str = '{"age": 20, "score": 88, "name": "Bob"}'
	json.loads(json_str)

jsontest()

class Teacher(object):
	def __init__(self,name,student):
		self.name = name
		self.student = student

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

def convert2json():
	s = Student('Bob',20,100)
	return json.dumps(s,default=student2dict)

def convert2json2():
	s = Student('Bob',20,100)
	return json.dumps(s,default=lambda obj: obj.__dict__)

def convert2json3():
	s = Student('Bob',20,100)
	t = Teacher('cao',s)
	return json.dumps(t,default=lambda obj: obj.__dict__)

print(convert2json())
print(convert2json2())
print(convert2json3())

def dict2student(dict):
	return Student(dict['name'],dict['age'],dict['score'])

def json2student():
	json_str = '{"age": 20, "score": 88, "name": "Bob"}'
	s = json.loads(json_str,object_hook=dict2student)
	print(s)

json2student()


def object2json(ob):
	return json.dumps(ob,default=lambda obj: obj.__dict__)

s = Student('Bob',20,100)
t = Teacher('cao',s)
print(object2json(t))


class Animal(object):
	def __init__(self,name):
		self.name = name

	def run():
		print('Animal run....')

class Dog(Animal):
	def __init__(self,name,dog_name):
		super().__init__(name)
		self.dog_name = dog_name

	def run():
		print('Dog run....')

dog = Dog('tom','muyangquan')
print(object2json(dog))




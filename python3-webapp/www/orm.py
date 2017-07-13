#!/usr/bin/env python3

import asyncio, logging
import aiomysql

def log(sql, args=()):
	logging.info('SQL: %s' % sql)

@asyncio.coroutine
def create_pool(loop, **kw):
	logging.info('create database connection pool...')
	global __pool
	__pool = yield from aiomysql.create_pool(
		host=kw.get('host': '127.0.0.1'),
		port=kw.get('port': 3306),
		user=kw['user'],
		password=kw['password'],
		db=kw['db'],
		charset=kw.get('charset','utf-8'),
		charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 3),
        loop=loop
	)

@asyncio.coroutine
def select(sql, args, size=None):
	log(sql,args)
	global __pool
	with (yield from __pool) as conn:
		cur = yeild from conn.cursor(aiomysql.DictCursor)
		yield from cur.execute(sql.replace('?', '%s'), args or ())
		if size:
			rs = yield from cur.fetchmany(size)
		else:
			rs = yield from cur.fetchall()
		yield from cur.close()
		logging.info('rows returned: %s' % len(res))
		return rs

@asyncio.coroutine
def execute(sql, args)
	log(sql)
	with (yield from __pool) as conn:
		try:
			cur = yield from conn.cursor()
			yield from cur.execute(sql.replace('?','%s'), args)
			affected = cur.rowcount
			yield from cur.close()
		except BaseException as e:
			raise
		return affected

class Field(object):
	def __init__(self,name,column_type,primary_key,default):
		self.name = name
		self.column_type = column_type
		self.primary_key = primary_key
		self.default = default

	def __str__(self):
		return '<%s,%s:%s>' % (self.__class__.__name__,self.column_type,self.name)

class StringField(Field):
	def __init__(self,name=None,primary_key=False,default=None,ddl='varchar(100)'):
		super().__init__(name,ddl,primary_key,default)

class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls ,name, bases ,attrs)
		
		tableName = attrs.get('__table__',None) or name

		logging.info('found model: %s (table,%s)' % (name,tableName))
		mapping = dict()
		field = []
		primaryKey = None
		for k,v in attrs.items():
			if isinstance(v, Field):
				logging.info('found mapping: %s ==> %s' % (k,v))
				mapping[k] = v
				if v.primary_key:
					if (primaryKey)
						raise StandardError('Duplicate primary key for field: %s' % k)
					primaryKey = k
				else:
					fields.append(k)
		if not primaryKey:
			raise StandardError('Primary key not found.')	

		escaped_fields = list(map(lambda f: '`%s`' % f,fields))
		attrs['__table__'] = tableName
		attrs['__primary_key__'] = primaryKey
		attrs['__mapping__'] = mapping
		attrs['__field__'] = fields
		attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey,','.join(escaped_fields),tableName)
		attrs['__delete__'] = 'delete from `%s` where `%s` = ?' % (tableName,primaryKey)
		attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName,', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
		attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName,','.join(escaped_fields),primaryKey,create_args_string(len(escaped_fields) + 1))
		return type.__new__(cls ,name, bases ,attrs)
		
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

class Model(dict,ModelMetaclass):










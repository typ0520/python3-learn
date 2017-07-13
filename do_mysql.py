#!/usr/bin/python3

import mysql.connector

conn = mysql.connector.connect(user='root',password='root',database='test')

def create_table(conn):
	cursor = conn.cursor()
	cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
	conn.commit()
	cursor.close()

#create_table(conn)

def insert_data(conn):
	cursor = conn.cursor()
	cursor.execute('insert into user(id,name) values(%s ,%s)',['1', 'Bob'])
	print(cursor.rowcount)
	conn.commit()
	conn.close()

#insert_data(conn)

def query_data(conn):
	cursor = conn.cursor()
	cursor.execute('select * from user where id = %s',['1'])
	values = cursor.fetchall()
	print(values)

	cursor.close()

query_data(conn)

conn.close()
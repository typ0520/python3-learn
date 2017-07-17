#!/usr/bin/env python3

import orm

from models import User, Blog, Comment

import asyncio

# async def test():
# 	await orm.create_pool(user='root', password='root', database='awesome')
# 	u = User(name='Test', email='test@qq.com', passwd='typ0520', image='about:black')
#     u.save()

# test()

# loop = asyncio.get_event_loop()

# orm.create_pool(loop,user='root', password='root', database='awesome')
# u = User(name='Test', email='test@qq.com', passwd='typ0520', image='about:black')
# u.save()

@asyncio.coroutine
def test_save(loop):
	yield from orm.create_pool(loop=loop, user='root', password='root', db='awesome')
	u = User(name='hi', email='hi@example.com',passwd='hi', image='about:blank')
	yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_save(loop))
loop.close()
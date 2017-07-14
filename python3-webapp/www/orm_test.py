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


def test():
    yield from orm.create_pool(user='www-data', password='www-data', database='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()

for x in test():
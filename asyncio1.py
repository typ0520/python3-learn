#!/usr/bin/env python3

import asyncio

@asyncio.coroutine
def hello():
	print('Hello world!')
	r = yield from asyncio.sleep(5)
	print('Hello again!')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(),hello()]))
loop.close()
import asyncio

async def hello():
	print('hello start')
	await asyncio.sleep(1)
	print('hello end')
	await asyncio.sleep(1)
	print('hello end2')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(),hello()]))
loop.close()
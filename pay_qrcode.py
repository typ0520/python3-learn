#!/usr/bin/env python3

import asyncio
from aiohttp import web

async def pay(request):
	#HTTPS://QR.ALIPAY.COM/FKX04870JYZA0EJ9GEJVDA
	#wxp://f2f0Znc5aKoTogU2Oq3nElll2yfbW3NLfVaZ
    headers = {
        'Location': 'http://www.baidu.com'
    }
    return web.Response(status=302, headers=headers)


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', pay)
    srv = await loop.create_server(app.make_handler(),'192.168.2.1', 8001)
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

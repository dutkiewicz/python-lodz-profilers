from aiohttp import web
import time
import json

routes = web.RouteTableDef()


@routes.get("/")
async def index(request):
    return web.Response(text="ok")


@routes.get("/search")
async def search(request):
    found = []
    for i in range(5):
        found.append(i_am_slow(i))
    response = json.dumps(found)
    return web.Response(text=response)


def i_am_slow(value):
    time.sleep(2)
    return value

from fastapi import APIRouter
from infra.http.IHttpServer import IHttpServer

class FastApiServer(IHttpServer):
    def __init__(self):
        self.router = APIRouter()

    def on(self, method, url, callback):
        self.router.add_api_route(url, methods=[method], endpoint=callback)

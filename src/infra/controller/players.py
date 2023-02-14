from application.get_players import GetPlayers
from infra.http.ihttp_server import IHttpServer

class PlayerController:
    def __init__(self, httpServer: IHttpServer, getPlayers: GetPlayers):
        self.httpServer = httpServer
        self.getPlayers: GetPlayers = getPlayers

        self.httpServer.on(url="/players", method="GET", callback=self.get_players)

    async def get_players(
        self,
    ):
        
        return self.getPlayers.execute()
from IHttpServer import IHttpServer
from IPlayerRepository import IPlayerRepository


class PlayerController:
    def __init__(self, httpServer: IHttpServer, player_data: IPlayerRepository):
        self.httpServer = httpServer
        self.player_data: IPlayerRepository = player_data

        self.httpServer.on(url="/players", method="GET", callback=self.get_players)

    async def get_players(
        self,
    ):
        return self.player_data.getPlayers()

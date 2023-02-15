from application.get_player import GetPlayer
from application.get_players import GetPlayers
from infra.http.ihttp_server import IHttpServer

class PlayerController:
    def __init__(self, httpServer: IHttpServer, getPlayers: GetPlayers, _get_player: GetPlayer):
        self.httpServer = httpServer
        self._get_players: GetPlayers = getPlayers
        self._get_player: GetPlayer = _get_player

        self.httpServer.on(url="/players", method="GET", callback=self.get_players)
        self.httpServer.on(url="/player/{player_id}", method="GET", callback=self.get_player)

    async def get_players(
        self,
    ):
        
        return self._get_players.execute()

    async def get_player(self, player_id: int):
        return self._get_player.execute(player_id)
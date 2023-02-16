from fastapi import HTTPException
from pydantic import BaseModel
from application.add_player_to_team import AddPlayerToTeam
from application.get_players_from_team import GetPlayersFromTeam
from infra.http.ihttp_server import IHttpServer


class TeamPlayer(BaseModel):
    team_id: int
    player_id: int


class TeamPlayerController:
    def __init__(
        self,
        httpServer: IHttpServer,
        _add_player_to_team: AddPlayerToTeam,
        _get_players_from_team: GetPlayersFromTeam,
    ):
        self.http_server = httpServer
        self._add_player_to_team: AddPlayerToTeam = _add_player_to_team
        self._get_players_from_team: GetPlayersFromTeam = _get_players_from_team

        self.http_server.on(
            method="POST", url="/teamPlayer", callback=self.add_player_to_team
        )
        self.http_server.on(method="GET", url="/teamPlayer/{team_id}", callback=self.get_players_from_team)

    def add_player_to_team(self, team_player: TeamPlayer):
        try:
            self._add_player_to_team.execute(team_player.team_id, team_player.player_id)
        except Exception as e:
            print(e.args[0])
            raise HTTPException(status_code=500)

    def get_players_from_team(self, team_id:int):
        return self._get_players_from_team.execute(team_id)

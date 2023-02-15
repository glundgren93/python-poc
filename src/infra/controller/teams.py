from pydantic import BaseModel

from application.create_team import CreateTeam
from application.get_team import GetTeam
from application.get_teams import GetTeams
from infra.http.ihttp_server import IHttpServer

class Team(BaseModel):
    teamName: str

class TeamController:
    def __init__(self, httpServer: IHttpServer, _create_team:CreateTeam, _get_teams: GetTeams, _get_team: GetTeam):
        self.httpServer = httpServer
        self._create_team: CreateTeam = _create_team
        self._get_teams: GetTeams = _get_teams
        self._get_team: GetTeam = _get_team

        self.httpServer.on(url="/teams", method="POST", callback=self.create_team, )
        self.httpServer.on(url="/teams", method="GET", callback=self.get_teams, )
        self.httpServer.on(url="/team/{team_id}", method="GET", callback=self.get_team, )

    async def create_team(
        self,
        team: Team
    ):
        return self._create_team.execute(team.teamName)

    async def get_teams(self):
        return self._get_teams.execute()

    async def get_team(self, team_id: int):
        print(team_id)
        return self._get_team.execute(team_id)
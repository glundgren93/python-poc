from CreateTeam import CreateTeam
from GetTeams import GetTeams
from IHttpServer import IHttpServer

from pydantic import BaseModel

class Team(BaseModel):
    teamName: str

class TeamController:
    def __init__(self, httpServer: IHttpServer, createTeam:CreateTeam, getTeams: GetTeams):
        self.httpServer = httpServer
        self.createTeam: CreateTeam = createTeam
        self.getTeams: GetTeams = getTeams

        self.httpServer.on(url="/teams", method="POST", callback=self.create_team, )
        self.httpServer.on(url="/teams", method="GET", callback=self.get_teams, )

    async def create_team(
        self,
        team: Team
    ):
        return self.createTeam.execute(team.teamName)

    async def get_teams(self):
        return self.getTeams.execute()
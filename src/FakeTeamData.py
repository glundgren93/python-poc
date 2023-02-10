from src.ITeamData import ITeamData
from src.Team import Team


class FakeTeamData(ITeamData):
    def __init__(self):
        self.teams = [
            Team(1, "Apex"),
            Team(2, "Apex subteam", 1),
            Team(3, "Falcons"),
        ]

    def getTeams(self):
        return self.teams

    def getTeam(self, team_id) -> Team:
        return next((x for x in self.teams if x.id == team_id), None)

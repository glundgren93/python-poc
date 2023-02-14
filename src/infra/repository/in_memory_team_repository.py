from domain.entities.team import Team
from domain.repository.iteam_repository import ITeamRepository

class FakeTeamRepository(ITeamRepository):
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

    def getSubTeams(self, team_id):
        return [team for team in self.teams if team.parent_id == team_id]

    def createTeam(self, team_name, parent_id):
        new_id = len(self.teams) + 1
        self.teams.append(Team(new_id, team_name, parent_id))
        return new_id
from IPlayerRepository import IPlayerRepository
from ITeamRepository import ITeamRepository


class GetTeams():
    def __init__(self, team_data):
        self.team_data: ITeamRepository = team_data

    def execute(self):
        teams = self.team_data.getTeams()

        return teams
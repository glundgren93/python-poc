from domain.repository.iteam_repository import ITeamRepository


class GetTeam():
    def __init__(self, team_data):
        self.team_data: ITeamRepository = team_data

    def execute(self, team_id):
        team = self.team_data.get_team(team_id=team_id)

        return team
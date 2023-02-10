from src.ITeamRepository import ITeamRepository


class CreateTeam():
    def __init__(self, team_data):
        self.team_data: ITeamRepository = team_data

    def execute(self, team_name, parent_id = None):
        new_id = self.team_data.createTeam(team_name, parent_id)

        return new_id
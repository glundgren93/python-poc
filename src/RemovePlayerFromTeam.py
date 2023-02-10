from src.IPlayerData import IPlayerData
from src.ITeamPlayerData import ITeamPlayerData
from src.ITeamData import ITeamData


class RemovePlayerFromTeam():
    def __init__(self, player_data, team_data, team_player_data):
        self.player_data: IPlayerData = player_data
        self.team_data: ITeamData = team_data
        self.team_player_data: ITeamPlayerData = team_player_data

    def execute(self, team_id, player_id):
        self.team_player_data.delete_team_player(team_id, player_id)

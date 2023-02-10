from src.IPlayerRepository import IPlayerRepository
from src.ITeamPlayerRepository import ITeamPlayerRepository
from src.ITeamRepository import ITeamRepository


class RemovePlayerFromTeam():
    def __init__(self, player_data, team_data, team_player_data):
        self.player_data: IPlayerRepository = player_data
        self.team_data: ITeamRepository = team_data
        self.team_player_data: ITeamPlayerRepository = team_player_data

    def execute(self, team_id, player_id):
        if self.team_data.getTeam(team_id) == None:
            raise Exception("Team does not exist")

        if self.player_data.getPlayer(player_id) == None:
            raise Exception("Player does not exist")

        self.team_player_data.delete_team_player(team_id, player_id)

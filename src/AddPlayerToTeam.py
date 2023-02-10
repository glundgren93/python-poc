from src.ITeamData import ITeamData
from src.ITeamPlayerData import ITeamPlayerData
from src.IPlayerData import IPlayerData


class AddPlayerToTeam:
    def __init__(self, player_data, team_data, team_player_data):
        self.player_data: IPlayerData = player_data
        self.team_data: ITeamData = team_data
        self.team_player_data: ITeamPlayerData = team_player_data

    def execute(self, team_id, player_id):
        if self.player_data.getPlayer(player_id) == None:
            raise Exception("Player does not exist")
            
        if self.team_data.getTeam(team_id) == None:
            raise Exception("Team does not exist")

        self.team_player_data.create_team_player(team_id, player_id)

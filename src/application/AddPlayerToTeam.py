

from domain.repository.IPlayerRepository import IPlayerRepository
from domain.repository.ITeamPlayerRepository import ITeamPlayerRepository
from domain.repository.ITeamRepository import ITeamRepository


class AddPlayerToTeam:
    def __init__(self, player_data, team_data, team_player_data):
        self.player_data: IPlayerRepository = player_data
        self.team_data: ITeamRepository = team_data
        self.team_player_data: ITeamPlayerRepository = team_player_data

    def execute(self, team_id, player_id):
        if self.player_data.getPlayer(player_id) == None:
            raise Exception("Player does not exist")
            
        if self.team_data.getTeam(team_id) == None:
            raise Exception("Team does not exist")

        self.team_player_data.create_team_player(team_id, player_id)

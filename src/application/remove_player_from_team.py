from domain.repository.iplayer_repository import IPlayerRepository
from domain.repository.iteam_player_repository import ITeamPlayerRepository
from domain.repository.iteam_repository import ITeamRepository


class RemovePlayerFromTeam():
    def __init__(self, player_data, team_data, team_player_data):
        self.player_data: IPlayerRepository = player_data
        self.team_data: ITeamRepository = team_data
        self.team_player_data: ITeamPlayerRepository = team_player_data

    def execute(self, team_id, player_id):
        if self.team_data.get_team(team_id) == None:
            raise Exception("Team does not exist")

        if self.player_data.get_player(player_id) == None:
            raise Exception("Player does not exist")

        self.team_player_data.delete_team_player(team_id, player_id)

from src.ITeamPlayerData import ITeamPlayerData
from src.PlayerTeam import PlayerTeam


class FakeTeamPlayerData(ITeamPlayerData):
    def __init__(self):
        self.playerTeams = []

    def create_team_player(self, team_id, player_id):
        userTeam = PlayerTeam(player_id, team_id)
        self.playerTeams.append(userTeam)

    def get_players_from_team(self, team_id):
        return [item for item in self.playerTeams if item.team_id == team_id]

    def get_teams_from_player(self, player_id):
        return [item for item in self.playerTeams if item.player_id == player_id]

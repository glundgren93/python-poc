from domain.entities.PlayerTeam import PlayerTeam
from domain.repository.ITeamPlayerRepository import ITeamPlayerRepository


class FakeTeamPlayerRepository(ITeamPlayerRepository):
    def __init__(self):
        self.playerTeams = []

    def create_team_player(self, team_id, player_id):
        userTeam = PlayerTeam(player_id, team_id)
        self.playerTeams.append(userTeam)

    def get_players_from_team(self, team_id):
        return [item for item in self.playerTeams if item.team_id == team_id]

    def get_teams_from_player(self, player_id):
        return [item for item in self.playerTeams if item.player_id == player_id]

    def delete_team_player(self, team_id, player_id):
        for i, player_team in enumerate(self.playerTeams):
            if player_team.team_id == team_id and player_team.player_id == player_id:
                del self.playerTeams[i]
                break
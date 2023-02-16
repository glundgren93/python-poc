from domain.repository.iteam_player_repository import ITeamPlayerRepository


class GetPlayersFromTeam():
    def __init__(self, team_player_repository: ITeamPlayerRepository):
        self.team_player_repository = team_player_repository

    def execute(self, team_id):
        return self.team_player_repository.get_players_from_team(team_id)
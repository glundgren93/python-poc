from abc import ABC, abstractmethod

class ITeamPlayerData(ABC):
    @abstractmethod
    def get_teams_from_player(player_id):
        pass

    @abstractmethod
    def get_players_from_team(team_id):
        pass

    @abstractmethod
    def create_team_player(team_id, player_id):
        pass


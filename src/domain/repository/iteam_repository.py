from abc import ABC, abstractmethod
from domain.entities.team import Team

class ITeamRepository(ABC):
    @abstractmethod
    def get_teams():
        pass

    @abstractmethod
    def get_team(self, team_id) -> Team:
        pass

    @abstractmethod
    def get_sub_teams(self, team_id):
        pass

    @abstractmethod
    def create_team(self, team_name, parent_id):
        pass
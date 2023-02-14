from abc import ABC, abstractmethod
from domain.entities.team import Team

class ITeamRepository(ABC):
    @abstractmethod
    def getTeams():
        pass

    @abstractmethod
    def getTeam(self, team_id) -> Team:
        pass

    @abstractmethod
    def getSubTeams(self, team_id):
        pass

    @abstractmethod
    def createTeam(self, team_name, parent_id):
        pass
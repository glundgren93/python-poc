from abc import ABC, abstractmethod

from src import Team


class ITeamRepository(ABC):
    @abstractmethod
    def getTeams():
        pass

    @abstractmethod
    def getTeam(team_id) -> Team:
        pass

    @abstractmethod
    def getSubTeams(team_id):
        pass

    @abstractmethod
    def createTeam(team_name, parent_id):
        pass
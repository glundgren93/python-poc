from abc import ABC, abstractmethod

from src import Team


class ITeamData(ABC):
    @abstractmethod
    def getTeams():
        pass

    @abstractmethod
    def getTeam(team_id) -> Team:
        pass

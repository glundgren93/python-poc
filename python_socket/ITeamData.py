from abc import ABC, abstractmethod

from python_socket import Team


class ITeamData(ABC):
    @abstractmethod
    def getTeams():
        pass

    @abstractmethod
    def getTeam(team_id) -> Team:
        pass

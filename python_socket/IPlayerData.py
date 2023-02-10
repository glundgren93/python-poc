from abc import ABC, abstractmethod

from python_socket import Player


class IPlayerData(ABC):
    @abstractmethod
    def getPlayers():
        pass

    @abstractmethod
    def getPlayer(email) -> Player:
        pass
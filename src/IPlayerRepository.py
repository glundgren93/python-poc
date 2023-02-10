from abc import ABC, abstractmethod

from src import Player


class IPlayerRepository(ABC):
    @abstractmethod
    def getPlayers():
        pass

    @abstractmethod
    def getPlayer(email) -> Player:
        pass
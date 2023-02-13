from abc import ABC, abstractmethod

from domain.entities.Player import Player



class IPlayerRepository(ABC):
    @abstractmethod
    def getPlayers():
        pass

    @abstractmethod
    def getPlayer(email) -> Player:
        pass

    @abstractmethod
    def createPlayer(email, role):
        pass
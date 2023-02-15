from abc import ABC, abstractmethod
from domain.entities.player import Player

class IPlayerRepository(ABC):
    @abstractmethod
    def get_players():
        pass

    @abstractmethod
    def get_player(email) -> Player:
        pass

    @abstractmethod
    def create_player(self, email, role):
        pass
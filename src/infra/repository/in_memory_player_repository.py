from domain.entities.player import Player
from domain.repository.iplayer_repository import IPlayerRepository

class FakePlayerRepository(IPlayerRepository):
    def __init__(self):
        self.players = [
            Player(1, "coach1", "coach"),
            Player(2, "coach2", "coach"),
            Player(3, "player1", "player"),
            Player(4, "player2", "player"),
        ]

    def getPlayers(self):
        return self.players

    def getPlayer(self, id):
        return next((x for x in self.players if x.id == id), None)

    def createPlayer(self, email, role):
        new_id = len(self.players) + 1
        self.teams.append(Player(new_id, email, role))

        return new_id
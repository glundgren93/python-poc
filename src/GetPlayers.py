from src.IPlayerRepository import IPlayerRepository


class GetPlayers():
    def __init__(self, player_data):
        self.player_data: IPlayerRepository = player_data

    def execute(self):
        players = self.player_data.getPlayers()

        return players
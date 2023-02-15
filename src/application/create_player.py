from domain.repository.iplayer_repository import IPlayerRepository

class CreatePlayer():
    def __init__(self, player_data):
        self.player_data: IPlayerRepository = player_data

    def execute(self, email, role):
        new_id = self.player_data.create_player(email, role)

        return new_id
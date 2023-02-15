from domain.repository.iplayer_repository import IPlayerRepository


class GetPlayer():
    def __init__(self, player_data):
        self.player_data: IPlayerRepository = player_data

    def execute(self, player_id):
        player = self.player_data.get_player(player_id)

        return player
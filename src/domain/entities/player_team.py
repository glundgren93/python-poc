from datetime import datetime

class PlayerTeam():
    def __init__(self, player_id, team_id):
        self.player_id = player_id
        self.team_id = team_id
        self.join_date = datetime.now()

    
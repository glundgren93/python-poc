from src.AddPlayerToTeam import AddPlayerToTeam
from src.FakePlayerData import FakePlayerData
from src.FakeTeamData import FakeTeamData
from src.FakeTeamPlayerData import FakeTeamPlayerData
from src.RemovePlayerFromTeam import RemovePlayerFromTeam

def test_remove_player_from_team():
    team_id = 1
    player_id = 1

    player_fake_data = FakePlayerData()
    team_fake_data = FakeTeamData()
    team_player_fake_data = FakeTeamPlayerData()

    add_player_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    add_player_to_team.execute(team_id, player_id)

    remove_player_from_team = RemovePlayerFromTeam(player_fake_data, team_fake_data, team_player_fake_data)
    remove_player_from_team.execute(team_id,player_id)

    players = team_player_fake_data.get_players_from_team(team_id)
    teams = team_player_fake_data.get_teams_from_player(player_id)

    assert len(teams) == 0
    assert len(players) == 0

def test_remove_player_from_team():
    team_id = 1
    player_id = 1
    player_id_2 = 2

    player_fake_data = FakePlayerData()
    team_fake_data = FakeTeamData()
    team_player_fake_data = FakeTeamPlayerData()

    add_player_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    add_player_to_team.execute(team_id, player_id)
    add_player_to_team.execute(team_id, player_id_2)

    remove_player_from_team = RemovePlayerFromTeam(player_fake_data, team_fake_data, team_player_fake_data)
    remove_player_from_team.execute(team_id,player_id)

    players = team_player_fake_data.get_players_from_team(team_id)
    teams = team_player_fake_data.get_teams_from_player(player_id)

    assert len(teams) == 0
    assert len(players) == 1
import pytest

from src.AddPlayerToTeam import AddPlayerToTeam
from src.FakePlayerData import FakePlayerData
from src.FakeTeamData import FakeTeamData
from src.FakeTeamPlayerData import FakeTeamPlayerData


def test_add_user_to_team():
    team_id = 1
    player_id = 1

    player_fake_data = FakePlayerData()
    team_fake_data = FakeTeamData()
    team_player_fake_data = FakeTeamPlayerData()

    add_user_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    add_user_to_team.execute(team_id, player_id)

    players = team_player_fake_data.get_players_from_team(team_id)
    teams = team_player_fake_data.get_teams_from_player(player_id)

    assert len(teams) == 1
    assert len(players) == 1


def test_add_multiple_players_to_team():
    team_id = 1
    player_id = 1
    player_to_be_added_id = 2

    player_fake_data = FakePlayerData()
    team_fake_data = FakeTeamData()
    team_player_fake_data = FakeTeamPlayerData()

    add_user_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    add_user_to_team.execute(team_id, player_id)
    add_user_to_team.execute(team_id, player_to_be_added_id)

    team_players_amount = team_player_fake_data.get_players_from_team(team_id)
    player_teams_amount = team_player_fake_data.get_teams_from_player(player_id)
    second_player_teams_amount = team_player_fake_data.get_teams_from_player(
        player_to_be_added_id
    )

    assert len(team_players_amount) == 2
    assert len(player_teams_amount) == 1
    assert len(second_player_teams_amount) == 1


def test_add_player_to_multiple_teams():
    team_id = 1
    second_team_id = 2
    third_team_id = 3
    player_id = 1

    player_fake_data = FakePlayerData()
    team_fake_data = FakeTeamData()
    team_player_fake_data = FakeTeamPlayerData()

    add_user_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    add_user_to_team.execute(team_id, player_id)
    add_user_to_team.execute(second_team_id, player_id)
    add_user_to_team.execute(third_team_id, player_id)

    team_players_amount = team_player_fake_data.get_players_from_team(team_id)
    second_team_players_amount = team_player_fake_data.get_players_from_team(team_id)
    third_team_players_amount = team_player_fake_data.get_players_from_team(team_id)
    player_teams_amount = team_player_fake_data.get_teams_from_player(player_id)

    assert len(team_players_amount) == 1
    assert len(second_team_players_amount) == 1
    assert len(third_team_players_amount) == 1
    assert len(player_teams_amount) == 3


def test_cannot_add_player_to_non_existing_team():
    with pytest.raises(Exception, match="Team does not exist"):
        team_id = 4
        player_id = 1

        player_fake_data = FakePlayerData()
        team_fake_data = FakeTeamData()
        team_player_fake_data = FakeTeamPlayerData()

        add_user_to_team = AddPlayerToTeam(
            player_fake_data, team_fake_data, team_player_fake_data
        )
        add_user_to_team.execute(team_id, player_id)


def test_cannot_add_non_existing_player_to_team():
    with pytest.raises(Exception, match="Player does not exist"):
        team_id = 1
        player_id = 45

        player_fake_data = FakePlayerData()
        team_fake_data = FakeTeamData()
        team_player_fake_data = FakeTeamPlayerData()

        add_user_to_team = AddPlayerToTeam(
            player_fake_data, team_fake_data, team_player_fake_data
        )
        add_user_to_team.execute(team_id, player_id)

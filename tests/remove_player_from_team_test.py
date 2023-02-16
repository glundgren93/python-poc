import pytest
from application.add_player_to_team import AddPlayerToTeam
from application.get_players_from_team import GetPlayersFromTeam
from application.remove_player_from_team import RemovePlayerFromTeam

from infra.repository.in_memory_player_repository import InMemoryPlayerRepository
from infra.repository.in_memory_team_player_repository import InMemoryTeamPlayerRepository
from infra.repository.in_memory_team_repository import InMemoryTeamRepository


def test_remove_player_from_team():
    team_id = 1
    player_id = 1

    player_fake_data = InMemoryPlayerRepository()
    team_fake_data = InMemoryTeamRepository()
    team_player_fake_data = InMemoryTeamPlayerRepository()

    add_player_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    get_players_from_team = GetPlayersFromTeam(team_player_fake_data)
    add_player_to_team.execute(team_id, player_id)

    remove_player_from_team = RemovePlayerFromTeam(player_fake_data, team_fake_data, team_player_fake_data)
    remove_player_from_team.execute(team_id,player_id)

    players = get_players_from_team.execute(team_id)
    teams = team_player_fake_data.get_teams_from_player(player_id)

    assert len(teams) == 0
    assert len(players) == 0

def test_remove_player_from_team():
    team_id = 1
    player_id = 1
    player_id_2 = 2

    player_fake_data = InMemoryPlayerRepository()
    team_fake_data = InMemoryTeamRepository()
    team_player_fake_data = InMemoryTeamPlayerRepository()

    add_player_to_team = AddPlayerToTeam(
        player_fake_data, team_fake_data, team_player_fake_data
    )
    get_players_from_team = GetPlayersFromTeam(team_player_fake_data)

    add_player_to_team.execute(team_id, player_id)
    add_player_to_team.execute(team_id, player_id_2)

    remove_player_from_team = RemovePlayerFromTeam(player_fake_data, team_fake_data, team_player_fake_data)
    remove_player_from_team.execute(team_id,player_id)

    players = get_players_from_team.execute(team_id)
    teams = team_player_fake_data.get_teams_from_player(player_id)

    assert len(teams) == 0
    assert len(players) == 1

def test_cannot_remove_player_from_non_existing_team():
    with pytest.raises(Exception, match="Team does not exist"):
        team_id = 4
        player_id = 1

        player_fake_data = InMemoryPlayerRepository()
        team_fake_data = InMemoryTeamRepository()
        team_player_fake_data = InMemoryTeamPlayerRepository()

        remove_player_from_team = RemovePlayerFromTeam(player_fake_data, team_fake_data, team_player_fake_data)
        remove_player_from_team.execute(team_id,player_id)

def test_cannot_remove_team_with_non_existing_player():
    with pytest.raises(Exception, match="Player does not exist"):
        team_id = 1
        player_id = 152

        player_fake_data = InMemoryPlayerRepository()
        team_fake_data = InMemoryTeamRepository()
        team_player_fake_data = InMemoryTeamPlayerRepository()

        remove_player_from_team = RemovePlayerFromTeam(player_fake_data, team_fake_data, team_player_fake_data)
        remove_player_from_team.execute(team_id,player_id)
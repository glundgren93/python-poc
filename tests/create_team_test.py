
from application.create_team import CreateTeam
from infra.repository.in_memory_team_repository import FakeTeamRepository


def test_create_team():
    team_fake_data = FakeTeamRepository()

    create_team = CreateTeam(team_fake_data)
    new_id = create_team.execute("Tigers")

    assert team_fake_data.getTeam(new_id).name == "Tigers"

from application.create_team import CreateTeam
from application.get_team import GetTeam
from infra.repository.in_memory_team_repository import InMemoryTeamRepository


def test_create_team():
    team_fake_data = InMemoryTeamRepository()

    create_team = CreateTeam(team_fake_data)
    get_team = GetTeam(team_fake_data)
    new_id = create_team.execute("Tigers")

    assert get_team.execute(new_id).name == "Tigers"
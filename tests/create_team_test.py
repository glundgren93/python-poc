
from application.CreateTeam import CreateTeam
from infra.repository.FakeTeamRepository import FakeTeamRepository


def test_create_team():
    team_fake_data = FakeTeamRepository()

    create_team = CreateTeam(team_fake_data)
    new_id = create_team.execute("Tigers")

    assert team_fake_data.getTeam(new_id).name == "Tigers"
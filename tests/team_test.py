from src.Team import Team

def test_create_team():
    team = Team(1, 'Apex')

    assert team.name == 'Apex'

def test_create_team_with_parent_team():
    team = Team(1, 'Apex')
    subteam = Team(2, 'Apex 2', 1)

    assert subteam.parent_id == 1    
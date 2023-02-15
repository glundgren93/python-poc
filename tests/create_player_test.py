from application.create_player import CreatePlayer
from application.get_player import GetPlayer
from infra.repository.in_memory_player_repository import InMemoryPlayerRepository


def test_create_player():
    player_fake_data = InMemoryPlayerRepository()

    create_player = CreatePlayer(
        player_fake_data
    )
    get_player = GetPlayer(player_fake_data)

    new_id = create_player.execute("teste@email.com", "coach")
    player = get_player.execute(new_id)
    
    assert player.email == "teste@email.com"
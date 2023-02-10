from python_socket.Player import Player

def test_create_player():
    player = Player(1, 'email@example.com', 'Coach')

    assert player.email == 'email@example.com'
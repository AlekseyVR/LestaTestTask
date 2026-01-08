import pytest
from rpg_game.controller import GameController

@pytest.fixture
def gc() -> GameController:
    return GameController()

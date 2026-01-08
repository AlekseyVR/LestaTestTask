import pytest
from rpg_game.controller import GameController


class BaseTest:

    @pytest.fixture
    def gc(self) -> GameController:
        return GameController()

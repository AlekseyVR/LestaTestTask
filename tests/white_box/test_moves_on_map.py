from unittest.mock import patch
import pytest
from tests.test_base_test import BaseTest


class DungeonMovesTest(BaseTest):

    def test_initial_position(self, gc):
        assert gc.position == 0, f"Start position is not 0. Actual result: {gc.position}"
        assert gc.dungeon[0].description == "Перед вами вход в подземелье.", \
            f"Room description don't correspond expected result. Actual result: {gc.dungeon[0].description}"

    def test_move_forward(self, gc):
        actual_position = 1
        expected_position = 2
        gc.position = actual_position
        available_actions = gc.show_actions(gc.dungeon[gc.position])
        gc.handle_choice('3', gc.dungeon[gc.position], available_actions)
        assert gc.position == expected_position

    def test_move_back(self, gc):
        actual_position = 2
        expected_position = 1
        gc.position = actual_position
        available_actions = gc.show_actions(gc.dungeon[gc.position])
        gc.handle_choice('2', gc.dungeon[gc.position], available_actions)
        assert gc.position == expected_position

    def test_exit_at_end(self, gc):
        gc.position = len(gc.dungeon) - 1
        available_actions = gc.show_actions(gc.dungeon[gc.position])
        with pytest.raises(SystemExit):
            with patch('builtins.input', return_value='Enter'):
                gc.handle_choice("4", gc.dungeon[gc.position], available_actions)

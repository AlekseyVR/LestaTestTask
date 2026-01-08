from rpg_game.controller import Actions


class DungeonMovesTest:

    def test_start_actions(self, gc):
        target_position = 0
        expected_actions = [Actions.MOVE_ON]
        available_actions = gc.show_actions(gc.dungeon[target_position])
        assert expected_actions == available_actions, (f"Unexpected action for 'St' position: "
                                                       f"{[i.value for i in set(expected_actions).difference(set(available_actions))]}")

    def test_actions_for_empty_room(self, gc):
        target_position = 1
        expected_actions = [Actions.RETURN_BACK, Actions.MOVE_ON]
        available_actions = gc.show_actions(gc.dungeon[target_position])
        assert expected_actions == available_actions, (f"Unexpected action for 'empty' room: "
                                                       f"{[i.value for i in set(expected_actions).difference(set(available_actions))]}")

    def test_move_back(self, gc):
        target_position = 2
        expected_actions = [Actions.ATTACK, Actions.RETURN_BACK]
        available_actions = gc.show_actions(gc.dungeon[target_position])
        assert expected_actions == available_actions, (f"Unexpected action for 'E' room: "
                                                       f"{[i.value for i in set(expected_actions).difference(set(available_actions))]}")

    def test_exit_at_end(self, gc):
        gc.position = len(gc.dungeon) - 1
        expected_actions = [Actions.RETURN_BACK, Actions.EXIT]
        available_actions = gc.show_actions(gc.dungeon[gc.position])
        assert expected_actions == available_actions, (f"Unexpected action for 'Ex' room: "
                                                       f"{[i.value for i in set(expected_actions).difference(set(available_actions))]}")

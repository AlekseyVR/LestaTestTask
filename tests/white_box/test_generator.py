from rpg_game.models.enemy import Enemy
from tests.test_base_test import BaseTest
from utils.files import load_from_json

class DungeonMovesTest(BaseTest):

    def test_create_player(self, gc):
        """ Check create user with the same data as player config json"""
        player = gc.player
        config_player = load_from_json("rpg_game/configs/player.json")
        assert player.hp == config_player["hp"]
        assert player.name in config_player["names"]
        assert player.death_description in config_player["death_descriptions"]
        assert player.description in config_player["descriptions"]

    def test_create_enemies(self):
        """ Check create enemies with the same data as enemy config json"""
        config_enemy = load_from_json("rpg_game/configs/enemies.json")
        enemies = Enemy.from_json()
        assert len(enemies) == len(config_enemy)
        for expected_enemy in config_enemy:
            enemy = next(i for i in enemies if i.name == expected_enemy['name'])
            assert enemy.name == expected_enemy['name']
            assert enemy.hp == expected_enemy['hp']
            assert enemy.description == expected_enemy['description']
            assert enemy.death_description == expected_enemy['death_description']

    def test_create_dungeon_structure(self, gc):
        """Check dungeon map structure"""
        expected_map = ("St", " ", "E", "E", " ", "E", "Ex")
        dungeon = gc.dungeon
        for index, item in enumerate(expected_map):
            room = dungeon[index]
            if item == "St":
                assert room.is_first, f"Room #{index+1} is not start room but must be"
            elif item == " ":
                assert not room.is_enemy_exists, "Enemy is exist but these room must be without enemy"
            elif item == "E":
                assert room.is_enemy_exists, "Enemy is not exist but these room must be with enemy"
            elif item == "Ex":
                assert room.is_last, "These room is not last but must be"
        assert len(dungeon) == len(expected_map), (f"Quantity rooms don't correspond with expected value:"
                                                   f"Actual: {len(expected_map)} and Expected: {len(dungeon)}")

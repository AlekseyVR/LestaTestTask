import pytest

from rpg_game.combat import auto_fight
from rpg_game.models.armor import Armor
from rpg_game.models.enemy import Enemy
from rpg_game.models.player import Player
from rpg_game.models.weapon import Weapon


class AutoFightTest:

    def create_player(self) -> Player:
        return Player.from_json()

    def test_player_wins(self):
        player = self.create_player()
        enemy = Enemy(name="Goblin", hp=5, description="Desc", death_description="Dead",
                      weapon=Weapon(name="Knife", description="Desc", damage=1, hit_chance=0),
                      armor=Armor(name="Armor", description="Desc", defense=0))
        auto_fight(player, enemy)
        assert enemy.hp <= 0, "Enemy lives but must be die"
        assert player.hp >= 0, "Player die but must be live"

    def test_player_fails(self):
        player = self.create_player()
        enemy = Enemy(name="Goblin", hp=15, description="Desc", death_description="Dead",
                      weapon=Weapon(name="Knife", description="Desc", damage=10, hit_chance=100),
                      armor=Armor(name="Armor", description="Desc", defense=0))
        auto_fight(player, enemy)
        assert enemy.hp >= 0, "Enemy die but must be live"
        assert player.hp <= 0, "Player live but must be die"

    # @pytest.mark.timeout(5)
    # def test_no_damage_if_armor_higher(self):
    #     expected_hp = 10
    #     player = Player(name="P", description="desc", hp=expected_hp, death_description="dd",
    #                weapon=Weapon(name="W", description="d", damage=2, hit_chance=100),
    #                armor=Armor(name="A", description="d", defense=5))
    #     enemy = Enemy(name="E", hp=expected_hp, description="desc", death_description="dead",
    #                   weapon=Weapon(name="W", description="d", damage=2, hit_chance=100),
    #                   armor=Armor(name="A", description="d", defense=5))
    #     auto_fight(player, enemy)
    #     assert player.hp == 10, f"Player hp was changed. Actual: {player.hp} Expected: {expected_hp}"
    #     assert enemy.hp == 10, f"Player hp was changed. Actual: {enemy.hp} Expected: {expected_hp}"

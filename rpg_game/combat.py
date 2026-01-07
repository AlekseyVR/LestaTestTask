import random
from enum import Enum

from rpg_game.models.enemy import Enemy
from rpg_game.models.player import Player

class StateOfLife(str, Enum):
    LIVE = "live"
    DEAD = "dead"


def auto_fight(player: Player, enemy: Enemy):
    while player.hp > 0 and enemy.hp > 0:
        # player step
        enemy_status = attack_with_random_hit_chance(player, enemy)
        if enemy_status == StateOfLife.DEAD:
            return
        player_status = attack_with_random_hit_chance(enemy, player)
        if player_status == StateOfLife.DEAD:
            return


def attack_with_random_hit_chance(character_1, character_2) -> StateOfLife:
    random_hit_chance = random.randint(0, 100)
    if character_1.weapon.hit_chance >= random_hit_chance:
        damage = max(character_1.weapon.damage - character_2.armor.defense, 0)
        character_2.hp -= damage
        print(f"{character_1.name} попал по {character_2.name}, нанесено урона: {damage}")
    else:
        print(f"{character_1.name} промахнулся")
    if character_2.hp <=0:
        return StateOfLife.DEAD
    return StateOfLife.LIVE

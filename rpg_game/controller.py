from enum import Enum
from symtable import Class

from rpg_game.generator import DungeonGenerator


class GameController:
    def __init__(self):
        self.dungeon = DungeonGenerator.dungeon
        self.player = DungeonGenerator.player
        self.position = 0

    def start(self):
        print(f"Добро пожаловать, {self.player.name}.")
        print(f"Описание игрока: {self.player.description}")
        while True:
            room = self.dungeon[self.position]
            print(f"Вы вошли в комнату: {room.description}")
            if room.is_enemy_exists and room.enemy.hp > 0:
                print(f"Вы видите врага {room.enemy.name}\n"
                      f"\tОписание вражины: {room.enemy.description}")
                self.show_actions(enemy_exists=True)
            else:
                self.show_actions(False)

    def show_actions(self, enemy_exists: bool):
        print("Доступные действия:")
        if enemy_exists:
            print(Actions.ATTACK)
        else:
            pass


class Actions(Enum, str):
    ATTACK = "1. Атаковать"
    RETURN_BACK = "2. Вернуться назад"
    EXIT = "3. Выйти из подземелья"

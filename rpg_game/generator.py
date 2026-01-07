import copy
import random

from rpg_game.models.enemy import Enemy, Enemies
from rpg_game.models.player import Player
from rpg_game.models.room import Room


class DungeonGenerator:
    # Карта должна быть представлена следующим образом (пример):
    __dungeon = ("St", " ", "E", "E", " ", "E", "Ex")
    __map_dungeon = None
    __player = None

    @property
    def dungeon(self) -> list[Room]:
        if self.__map_dungeon is None:
            self.__map_dungeon = self.create_dungeon()
        return self.__map_dungeon

    @property
    def player(self) -> Player:
        if self.__player is None:
            self.__player = self.__create_player()
        return self.__player

    @staticmethod
    def __create_player() -> Player:
        return Player.from_json()

    @staticmethod
    def __create_enemies():
        return Enemies().equip()

    def create_dungeon(self) -> list[Room]:
        rooms: list[Room] = Room.from_json()
        enemies: list[Enemy] = self.__create_enemies()
        dungeon = []
        for cell in self.__dungeon:
            if cell == "St":
                dungeon.append(Room(description="Перед вами вход в подземелье.", is_first=True, is_last=False))
            elif cell == "Ex":
                dungeon.append(Room(description="Вы видите свет, кажется это выход.", is_first=False, is_last=True))
            elif cell == "E":
                dungeon.append(Room(description=random.choice([i.description for i in rooms]),
                                    enemy=copy.deepcopy(random.choice(enemies)),
                                    is_first=False, is_last=False))
            else:
                dungeon.append(Room(description=random.choice([i.description for i in rooms]),
                                    is_first=False, is_last=False))
        return dungeon



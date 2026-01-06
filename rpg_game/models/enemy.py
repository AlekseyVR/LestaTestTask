import json
import random
from dataclasses import dataclass, field

from rpg_game.models.armor import Armor
from rpg_game.models.weapon import Weapon
from utils.files import load_from_json


@dataclass
class Enemy:
    name: str
    hp: int
    description: str
    death_description: str
    weapon: Weapon | None = field(default=None)
    armor: Armor | None = field(default=None)

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/enemies.json") -> list["Enemy"]:
        data = load_from_json(path)
        return [cls(**i) for i in data]


class Enemies:
    __equip_enemies: list[Enemy] = None

    @property
    def equip(self) -> list["Enemy"]:
        if self.__equip_enemies is None:
            self.__equip_enemies = Enemy.from_json()
        for enemy in self.__equip_enemies:
            if enemy.weapon is None:
                enemy.weapon = random.choice(Weapon.from_json())
            if enemy.armor is None:
                enemy.armor = random.choice(Armor.from_json())
        return self.__equip_enemies

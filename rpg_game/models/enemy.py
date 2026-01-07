import random
from dataclasses import dataclass, field

from rpg_game.models.armor import Armor, Armors
from rpg_game.models.weapon import Weapon, Weapons
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
    equip_enemies: list[Enemy] = None

    def equip(self):
        if self.equip_enemies is None:
            self.equip_enemies = Enemy.from_json()
        for enemy in self.equip_enemies:
            if enemy.weapon is None:
                enemy.weapon = random.choice(Weapons.from_json().weapons)
            if enemy.armor is None:
                enemy.armor = random.choice(Armors.from_json().armors)
        return self.equip_enemies

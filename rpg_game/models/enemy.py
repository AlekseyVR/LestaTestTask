import copy
import random
from dataclasses import dataclass, field

from rpg_game.models.armor import Armor, Armors
from rpg_game.models.base_character import BaseCharacter
from rpg_game.models.weapon import Weapon, Weapons
from utils.files import load_from_json


@dataclass
class Enemy(BaseCharacter):
    name: str
    hp: int
    description: str
    death_description: str
    weapon: Weapon | None = field(default=None)
    armor: Armor | None = field(default=None)

    max_hp: int = field(init=False, default=None)

    def __post_init__(self):
        self.max_hp = self.hp

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/enemies.json") -> list["Enemy"]:
        data = load_from_json(path)
        return [cls(**i) for i in data]


class Enemies:
    __equipped: list[Enemy] | None = None

    def equip(self) -> list[Enemy]:
        if self.__equipped is None:
            raw = Enemy.from_json()
            self.__equipped: list = []
            for equip in raw:
                # if armor / defense not specified - generate random from config
                weapon = equip.weapon if equip.weapon else random.choice(Weapons.from_json().weapons)
                armor = equip.armor if equip.armor else random.choice(Armors.from_json().armors)
                # needs copy because each enemy can has link on the same obj weapon or armor
                self.__equipped.append(
                    Enemy(
                        name=equip.name,
                        hp=equip.hp,
                        description=equip.description,
                        death_description=equip.death_description,
                        weapon=copy.deepcopy(weapon),
                        armor=copy.deepcopy(armor)
                    )
                )
            return self.__equipped
""" Data model based on config 'rpg_game/configs/player.json'"""

import random
from dataclasses import dataclass, field

from rpg_game.models.armor import Armor
from rpg_game.models.base_character import BaseCharacter
from rpg_game.models.weapon import Weapon
from utils.files import load_from_json


@dataclass
class Player(BaseCharacter):
    hp: int
    weapon: Weapon
    armor: Armor
    names: list[str] | None = field(default=None)
    descriptions: list[str] | None = field(default=None)
    death_descriptions: list[str] | None = field(default=None)

    max_hp: int = field(init=False, default=None)
    name: str = field(init=False, default=None)
    description: str = field(init=False, default=None)
    death_description: str = field(init=False, default=None)

    def __post_init__(self):
        self.name = random.choice(self.names)
        self.description = random.choice(self.descriptions)
        self.death_description = random.choice(self.death_descriptions)
        self.max_hp = self.hp

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/player.json") -> "Player":
        data = load_from_json(path)
        data["weapon"] = Weapon(**data["weapon"])
        data["armor"] = Armor(**data["armor"])
        return cls(**data)

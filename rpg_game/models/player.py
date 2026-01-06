from dataclasses import dataclass

from rpg_game.models.armor import Armor
from rpg_game.models.weapon import Weapon
from utils.files import load_from_json


@dataclass
class Player:
    name: str
    description: str
    hp: int
    weapon: Weapon
    armor: Armor

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/player.json") -> "Player":
        data = load_from_json(path)
        return cls(**data)
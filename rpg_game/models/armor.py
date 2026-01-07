""" Data model based on config 'rpg_game/configs/armor.json'"""

from dataclasses import dataclass, field
from utils.files import load_from_json


@dataclass
class Armor:
    name: str
    defense: int
    description: str | None = field(default=None)

@dataclass
class Armors:
    armors: list[Armor]

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/armor.json") -> "Armors":
        data = load_from_json(path)
        data["armors"] = [Armor(**armor) for armor in data["armors"]]
        return cls(**data)

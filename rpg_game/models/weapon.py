from dataclasses import dataclass

from utils.files import load_from_json


@dataclass
class Weapon:
    name: str
    description: str
    damage: int
    hit_chance: int

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/weapons.json") -> list["Weapon"]:
        data = load_from_json(path)
        return [cls(**i) for i in data]



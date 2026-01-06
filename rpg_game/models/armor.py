from dataclasses import dataclass

from utils.files import load_from_json


@dataclass
class Armor:
    name: str
    description: str
    defense: int

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/armor.json") -> list["Armor"]:
        data = load_from_json(path)
        return [cls(**i) for i in data]

from dataclasses import dataclass, field
from utils.files import load_from_json


@dataclass
class Weapon:
    name: str
    damage: int
    hit_chance: int
    description: str | None = field(default=None)

@dataclass
class Weapons:
    weapons: list[Weapon]

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/weapons.json") -> "Weapons":
        data = load_from_json(path)
        data["weapons"] = [Weapon(**weapon) for weapon in data["weapons"]]
        return cls(**data)

from dataclasses import dataclass, field

from rpg_game.models.enemy import Enemy
from utils.files import load_from_json


@dataclass
class Room:
    description: str
    enemy: Enemy | None = field(default=None)

    @classmethod
    def from_json(cls, path: str = "rpg_game/configs/rooms.json") -> list["Room"]:
        data = load_from_json(path)
        return [cls(description=i) for i in data]

class GamePropertyRoom(Room):
    is_first: bool
    is_last: bool

    @property
    def is_enemy_exists(self) -> bool:
        return bool(self.enemy)

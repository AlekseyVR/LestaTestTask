from dataclasses import dataclass, field
from rpg_game.models.armor import Armor
from rpg_game.models.weapon import Weapon


@dataclass
class BaseCharacter:
    hp: int
    name: str | None = field(default=None)
    description: str | None = field(default=None)
    death_description: str | None = field(default=None)
    weapon: Weapon | None = field(default=None)
    armor: Armor | None = field(default=None)

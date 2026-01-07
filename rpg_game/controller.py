from enum import Enum

from rpg_game.combat import auto_fight
from rpg_game.models.room import Room
from rpg_game.generator import DungeonGenerator


class Actions(str, Enum):
    ATTACK = "1. Атаковать"
    RETURN_BACK = "2. Вернуться назад"
    MOVE_ON = "3. Пойти дальше"
    EXIT = "4. Выйти из подземелья"


class GameController:
    def __init__(self):
        self.dungeon = DungeonGenerator().dungeon
        self.player = DungeonGenerator().player
        self.position = 0

    input_choose_action: str = "Выберите действие:"
    choose_action_title: str = "Выберите одну цифру из доступных действий:"

    def start(self):
        print(f"Добро пожаловать, {self.player.name}.")
        print(f"\tОписание игрока: {self.player.description}")
        while True:
            room = self.dungeon[self.position]
            print(f"Вы вошли в комнату: {room.description}")
            if room.is_enemy_exists and room.enemy.hp > 0:
                print(f"Вы видите врага {room.enemy.name}\n"
                      f"\tОписание вражины: {room.enemy.description}")
                available_actions = self.show_actions(dungeon_room=room)
                player_input = input(self.input_choose_action)
                self.handle_choice(player_input, room, available_actions)
            else:
                available_actions = self.show_actions(dungeon_room=room)
                player_input = input(self.input_choose_action)
                self.handle_choice(player_input, room, available_actions)

    def show_actions(self, dungeon_room: Room) -> list["Actions"]:
        available_actions: list = []
        if dungeon_room.is_enemy_exists and dungeon_room.enemy.hp > 0:
            available_actions.append(Actions.ATTACK)
            if not dungeon_room.is_first:
                # If is current room is not "St"
                available_actions.append(Actions.RETURN_BACK)
        else:
            if not dungeon_room.is_first: # Return back
                available_actions.append(Actions.RETURN_BACK)
            if (not dungeon_room.is_last and
                    not dungeon_room.is_enemy_exists or (dungeon_room.is_enemy_exists and dungeon_room.enemy.hp <= 0)):
                # Move on / continue
                # room is not last OR enemy doesn't exist in room OR (Enemy exist, but he is already die)
                available_actions.append(Actions.MOVE_ON)
            if dungeon_room.is_last: # Exit
                available_actions.append(Actions.EXIT)
        print(self.choose_action_title)
        [print('\t', action.value) for action in available_actions]
        return available_actions

    def handle_user_input(self, user_input: str, actions: list['Actions']):
        available_actions = [action.value[0] for action in actions]
        while user_input not in available_actions:
            print(f"Вы ввели неподдерживаемое значение: {user_input}")
            print(self.choose_action_title)
            [print('\t', action.value) for action in actions]
            user_input = input(self.input_choose_action)
        return user_input

    def handle_choice(self, choice: str, dungeon_room: Room, actions: list['Actions']):
        user_input = self.handle_user_input(choice, actions)
        if user_input == "1":
            auto_fight(self.player, dungeon_room.enemy)
            if self.player.hp <= 0:
                self.close_dungeon(f"{self.player.name} погиб в бою")
            elif dungeon_room.enemy.hp <= 0:
                print(dungeon_room.enemy.death_description)
        elif user_input == "2":
            self.position -= 1
        elif user_input == "3":
            self.position += 1
        elif user_input == "4":
            self.close_dungeon("Вы выходите из подземелья")

    @staticmethod
    def close_dungeon(*args):
        [print(message) for message in args]
        input("Нажмите Enter для продолжения")
        exit()

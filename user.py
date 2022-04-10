import re
import random
from game_field import GameField
from letters import Letter
from dot import Dot
from game_exceptions import BoardException


class Player:
    def __init__(self, board: GameField, enemy):
        self.board = board
        self.enemy = enemy

    def ask_target(self):
        raise NotImplementedError

    def move(self):
        while True:
            try:
                target = self.ask_target()
                repeat = self.enemy.board.strike(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask_target(self) -> Dot:
        target = Dot(x=random.randint(0, 5), y=random.randint(0, 5))
        print(f"Компьютер стреляет в поле {target}")
        return target


class User(Player):
    """
        Класс описывает пользователя
    """
    PATTERN = r"^([a-fA-F]+[0-9]|[0-9]+[a-fA-F])$"

    def ask_target(self) -> Dot:
        """ Получить у пользователя точку для выстрела. """
        print("Ваш ход")
        while True:
            coord = input("Введите координаты: ").replace(" ", "")
            if not re.match(User.PATTERN, coord):
                print("Получены неверные координаты!\n"
                      "Координат должно быть ровно две, буква от A до F и цифра от 1 до 6.")
                continue
            digit = re.findall('[1-6]', coord)[0]
            letter = re.findall('[a-fA-F]', coord)[0]
            print(f"Буква: {letter}, цифра: {digit}")
            return Dot(x=int(digit)-1, y=Letter[letter].value)


target = User(GameField(6), 1).ask_target()
print(target)


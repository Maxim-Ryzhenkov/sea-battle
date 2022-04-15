import re
import random
from game_field import GameField
from letters import Letter
from dot import Dot
from game_exceptions import BoardException


class Player:
    def __init__(self, board: GameField):
        self.board = board
        self.enemy = None
        self.name = None

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

    def set_enemy(self, enemy):
        """ Назначить противника. """
        self.enemy = enemy


class AI(Player):
    def __init__(self, board: GameField):
        super().__init__(board)
        self.name = 'компьютер'

    def ask_target(self) -> Dot:
        target = Dot(x=random.randint(0, 5), y=random.randint(0, 5))
        print(f"Компьютер стреляет в поле {target}")
        return target


class User(Player):
    """
        Класс описывает пользователя
    """
    PATTERN = r"^([a-fA-F]+[0-9]|[0-9]+[a-fA-F])$"

    def __init__(self, board: GameField):
        super().__init__(board)
        self.name = 'пользователь'

    def ask_target(self) -> Dot:
        """ Получить у пользователя точку для выстрела. """
        print("Ваш ход")
        while True:
            coord = input("Введите координаты: ").replace(" ", "")
            pattern_verification = re.match(User.PATTERN, coord)
            digit = re.findall('[1-6]', coord)
            letter = re.findall('[a-fA-F]', coord)
            if not all(condition for condition in (pattern_verification, digit, letter)):
                print("Получены неверные координаты!\n"
                      "Координат должно быть ровно две, буква от A до F и цифра от 1 до 6.")
                continue
            print(f"Буква: {letter[0]}, цифра: {digit[0]}")
            return Dot(x=int(digit[0])-1, y=Letter[letter[0]].value)


if __name__ == "__main__":

    """ Для отладки. """
    from game import Game
    user = User(Game().get_random_board())
    user.ask_target()

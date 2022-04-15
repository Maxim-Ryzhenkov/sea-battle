import enum
from random import randint, shuffle

from ship import Ship
from game_field import GameField
from user import User, AI
from game_exceptions import BoardWrongShipException


class Player(enum.Enum):
    user = 0
    ai = 1


class Game:
    def __init__(self, board_size=6):
        self.board_size = board_size
        self.user = User(board=self.get_random_board())
        self.ai = AI(board=self.get_random_board())
        self.user.set_enemy(enemy=self.ai)
        self.ai.set_enemy(enemy=self.user)
        self.user.board.hide = False
        self.ai.board.hide = True
        self.current_player = self.user

    def switch_player(self):
        """ Сменить активного игрока. """
        self.current_player = self.user if self.current_player == self.ai else self.ai

    def greet(self):
        print("-------------------------")
        print("Приветствуем вас")
        print("в игре")
        print("морской бой")
        print("-------------------------")
        print("формат ввода координаты - цифра и буква. Пробелы роли не играют.")
        print("буква - номер строки")
        print("цифра - номер столбца")

    def try_board(self) -> GameField or None:
        board = GameField(size=self.board_size)
        ships_sizes = [Ship.SIZE.small,
                       Ship.SIZE.small,
                       Ship.SIZE.small,
                       Ship.SIZE.small,
                       Ship.SIZE.medium,
                       Ship.SIZE.medium,
                       Ship.SIZE.large]
        shuffle(ships_sizes)
        for ship_size in ships_sizes:
            for _ in range(2000):
                free_dot = board.get_random_free_dot()
                if not free_dot:
                    return None  # Вернуть None если на поле нет свободных точек
                ship = Ship(bow_location=free_dot,
                            size=ship_size,
                            orientation=Ship.ORIENTATION(randint(0, 1)))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        return board

    def get_random_board(self) -> GameField:
        board = None
        while not board:
            board = self.try_board()
        return board

    def render_boards(self):
        print("-" * 20)
        print("Доска пользователя:")
        self.user.board.render()
        print("-" * 20)
        print("Доска компьютера:")
        self.ai.board.render()

    def loop(self):
        while True:
            self.render_boards()
            print(f"Ходит {self.current_player.name}!")
            repeat = self.current_player.move()
            print(f"Кораблей у пользователя: {self.user.board.live_ships}")
            print(f"Кораблей у компьютера: {self.ai.board.live_ships}")
            if self.current_player.enemy.board.live_ships == 0:
                print("-" * 20)
                print(f"{self.current_player.name.capitalize()} выиграл!")
                break
            if not repeat:
                self.switch_player()


if __name__ == "__main__":

    Game().loop()


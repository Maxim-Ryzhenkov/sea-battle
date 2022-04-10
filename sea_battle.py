import game_exceptions as exceptions
from game_field import GameField


class Game:
    def __init__(self):
        self.user_board = self.get_random_board()
        self.ai_board = self.get_random_board()

    def greet(self):
        print("Морской бой!")

    def get_random_board(self) -> GameField:
        pass

    def exit(self):
        print("Игра прервана пользователем!")
        exit(0)

    def loop(self):
        pass

    def start(self):
        self.greet()
        self.loop()


if __name__ == "__main__":
    pass


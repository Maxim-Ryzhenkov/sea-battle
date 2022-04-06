from ship import Ship


class GameField:
    def __init__(self, size):
        self.size = size
        self.size_index = list(range(self.size))
        self.ships = []

    def render(self):
        """ Нарисовать игровое поле. """
        print(f"    {'  '.join(map(str, self.size_index))}")
        print(f"  {'---' * self.size}")
        field = [row.copy() for row in self.field]
        for number in self.size_index:
            line = '  '.join(map(lambda point: point.state.sign, field[number]))
            print(f"{Letters(number).name} | {line}")

    def set_ship(self):
        pass
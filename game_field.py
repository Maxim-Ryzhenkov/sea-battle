# coding: utf-8

import enum
import itertools

from ship import Ship
from dot import Dot


def blue_background(text, disabled=True):
    if disabled:
        return text
    return f"\033[44m{text}\033[0m"


def yellow_color(text):
    return f"\033[31m{text}\033[0m"


class Letter(enum.Enum):
    """
        Перечисление букв-индексов, по вертикали игрового поля.
    """
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5


class Symbol(enum.Enum):
    """
        Перечисление состояний точек игрового поля.
    """
    sea = blue_background("~")
    busy = blue_background(yellow_color("+"))
    unknown = "unknown"
    under_fire = "░"


class GameField:
    def __init__(self, size=6, hide=True):
        self.size = size
        self.hide = hide
        self.size_index = list(range(self.size))
        self.field = [[Symbol.sea.value for line_number in self.size_index] for column_number in self.size_index]
        self.busy_dots = []
        self.ships = []
        self.destroyed_ships = 0

    def is_inside(self, dot: Dot) -> bool:
        """ Проверить, что точка принадлежит игровому полю. """
        return all(coord in range(self.size) for coord in [dot.x, dot.y])

    def is_outside(self, dot: Dot) -> bool:
        """ Проверить, что точка НЕ принадлежит игровому полю. """
        return not self.is_inside(dot)

    def _get_copy_for_rendering(self) -> list:
        """ Получить копию игрового поля для отрисовки. """
        field = self.field.copy()
        for line in self.size_index:
            for column in self.size_index:
                coord = (line, column)
                symbol = Symbol.busy.value if coord in self.busy_dots else Symbol.sea.value
                field[column][line] = symbol
        return field

    def render(self):
        """ Нарисовать игровое поле. """
        field = []
        header = f"   | {' | '.join(map(str, range(1, self.size + 1)))} |"
        field.append(header)
        for number, row in enumerate(self._get_copy_for_rendering()):
            line_index = f"{Letter(number).name}  {blue_background('| ')}"
            line = f"{blue_background(' | ').join(row)}{blue_background(' |')}"
            line = line_index + blue_background(line)
            field.append(line)
        for line in field:
            print(line)

    def countur(self, ship: Ship) -> set:
        """ Возвращает список точек, занятых кораблем и вокруг него. """
        busy_dots = []
        for dot in ship.dots:
            countur_dots = tuple(itertools.product(range(dot.x - 1, dot.x + 2), range(dot.y - 1, dot.y + 2)))
            countur_dots = [dot for dot in countur_dots if game_field.is_inside(Dot(dot[0], dot[1]))]
            busy_dots.extend(countur_dots)
        self.busy_dots.extend(set(busy_dots))
        return set(busy_dots)

    def add_ship(self):
        """ Добавить корабль на доску. """
        pass

    @property
    def live_ships(self):
        return len(self.ships)

    def strike(self, x, y):
        """ Выстрелить по доске. """
        pass


if __name__ == "__main__":
    game_field = GameField()
    dot = Dot(4, 1)
    ship = Ship(size=Ship.SIZE.large, orientation=Ship.ORIENTATION.horizontal, bow_location=dot)

    print(game_field.countur(ship))
    print(game_field.render())

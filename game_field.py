# coding: utf-8

import enum
import itertools
from random import randint

from ship import Ship
from dot import Dot
from letters import Letter
from game_exceptions import BoardOutException, BoardWrongShipException, BoardUsedException


def blue_background(text, disabled=True):
    """ Окрасить текст в синий цвет """
    if disabled:
        return text
    return f"\033[44m{text}\033[0m"


class Color(enum.Enum):
    """ Перечисление цветов. """
    red = 31
    blue = 36


def colorize(text: str, color: Color):
    return f"\033[{color.value}m{text}\033[0m"


class Symbol(enum.Enum):
    """
        Перечисление состояний точек игрового поля.
    """
    sea = colorize("~", Color.blue)
    busy = colorize(".", Color.red)
    ship = "■"
    unknown = "░"
    under_fire = colorize("X", Color.red)


class GameField:
    def __init__(self, size=6, hide=True):
        self.size = size
        self.hide = hide
        self.size_index = list(range(self.size))
        self.field = [[Symbol.sea.value for column_number in self.size_index] for line_number in self.size_index]
        self.busy_dots = []
        self.already_shot = []
        self.ships = []
        self.destroyed_ships = 0

    def is_inside(self, dot: Dot) -> bool:
        """ Проверить, что точка принадлежит игровому полю. """
        return all(coord in range(self.size) for coord in [dot.x, dot.y])

    def is_outside(self, dot: Dot) -> bool:
        """ Проверить, что точка НЕ принадлежит игровому полю. """
        return not self.is_inside(dot)

    def countur(self, ship: Ship) -> list:
        """ Возвращает список точек, занятых кораблем и вокруг него. """
        countur = []
        for dot in ship.dots:
            countur_coord = tuple(itertools.product(range(dot.x - 1, dot.x + 2), range(dot.y - 1, dot.y + 2)))
            countur_dots = [Dot(x, y) for x, y in countur_coord if
                            self.is_inside(Dot(x, y)) and
                            Dot(x, y) not in ship.dots and
                            Dot(x, y) not in countur]
            countur.extend(countur_dots)
        return countur

    def add_ship(self, ship: Ship, verbose=False):
        """ Добавить корабль на доску. """
        if any(self.is_outside(dot) or dot in self.busy_dots for dot in ship.dots):
            raise BoardWrongShipException
        self.update_field(dots=ship.dots, symbol=Symbol.ship)
        self.ships.append(ship)
        self.busy_dots.extend(self.countur(ship))
        self.busy_dots.extend(ship.dots)
        if verbose:
            self.update_field(dots=self.countur(ship), symbol=Symbol.busy)

    @property
    def live_ships(self) -> int:
        """ Количество живых кораблей на поле. """
        return len([ship for ship in self.ships if ship.is_alive()])

    def strike(self, dot: Dot) -> bool:
        """ Выстрелить по указанной точке доски. """
        if self.is_outside(dot):
            raise BoardOutException
        if dot in self.already_shot:
            raise BoardUsedException
        self.already_shot.append(dot)

        repeat_strike = False

        for ship in self.ships:
            if ship.is_hit(dot):
                ship.health -= 1
                self.update_field(dots=[dot, ], symbol=Symbol.under_fire)
                self.already_shot.append(dot)
                if ship.is_alive():
                    print("Корабль подбит!")
                    repeat_strike = True
                else:
                    print("Корабль уничтожен!")
                    self.already_shot.extend(self.countur(ship))
                    self.update_field(dots=[dot, ], symbol=Symbol.under_fire)
                    self.update_field(dots=self.countur(ship), symbol=Symbol.busy)
                    repeat_strike = True
                return repeat_strike
        self.update_field(dots=[dot, ], symbol=Symbol.busy)
        print("Промах.")
        return repeat_strike

    def update_field(self, dots: list, symbol: Symbol) -> None:
        """ Обновить символы на игровом поле. """
        for dot in dots:
            self.field[dot.x][dot.y] = symbol.value

    def render(self):
        """ Нарисовать игровое поле. """
        field_image = []
        header = f"   | {' | '.join(map(str, range(1, self.size + 1)))} |"
        field_image.append(header)
        field = self.field.copy()
        field = tuple(zip(*field[::-1]))  # Разворачиваю поле, чтобы ось X была горизонтальна, а Y - вертикальна.
        for y in self.size_index:
            line_index = f"{Letter(y).name}  {blue_background('| ')}"
            field_line = field[y][::-1]
            if self.hide:
                field_line = [point.replace(Symbol.ship.value, Symbol.sea.value) for point in field_line]
            field_line = f"{blue_background(' | ').join(field_line)}{blue_background(' |')}"
            line = line_index + blue_background(field_line)
            field_image.append(line)

        for line in field_image:
            print(line)

    def get_random_free_dot(self):
        for _ in range(2000):
            dot = Dot(x=randint(0, self.size-1), y=randint(0, self.size-1))
            if dot not in self.busy_dots:
                return dot
        return None


if __name__ == "__main__":
    game_field = GameField()
    ship1 = Ship(size=Ship.SIZE.medium, orientation=Ship.ORIENTATION.horizontal, bow_location=Dot(x=0, y=0))
    ship2 = Ship(size=Ship.SIZE.medium, orientation=Ship.ORIENTATION.vertical, bow_location=Dot(4, 2))
    game_field.add_ship(ship1, verbose=False)
    print(ship1.dots)
    game_field.add_ship(ship2, verbose=False)
    game_field.render()
    game_field.strike(Dot(x=0, y=0))
    game_field.render()
    game_field.strike(Dot(x=1, y=0))
    game_field.render()

from dot import Dot
from game_field import GameField
from enum import Enum


class ShipOrientation(Enum):
    """
        Перечисление возможных ориентаций корабля на игровом поле.
    """
    vertical = 0
    horizontal = 1


class ShipSize(Enum):
    """
        Перечисление доступных размеров корабля.
    """
    small = 1
    medium = 2
    large = 3


class Ship:
    """
        Класс описывает корабль на игровом поле.
    """
    _health = None

    def __init__(self, location: tuple, size: ShipSize, orientation: ShipOrientation):
        self.location = location
        self.size = size
        self.orientation = orientation
        self.health = self.size.value
        self.dots = self.get_dots()

    def get_dots(self) -> list:
        """ Получить точки в которых находится корабль. """
        dots = []
        for n in range(self.size.value):
            if self.orientation == ShipOrientation.vertical:
                dot = Dot(vertical_coord=self.location[0] + n, horizontal_coord=self.location[1])
            else:
                dot = Dot(vertical_coord=self.location[0], horizontal_coord=self.location[1] + n)
            if dot not in GameField:
                raise GameField.OutOfFieldError(f"Точка {dot} находится вне игрового поля.")
            dots.append(dot)
        return dots

    def is_alive(self) -> bool:
        """ Жив ли корабль. """
        return self.health < 0

import enum
import random

from dot import Dot
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
    SIZE = ShipSize
    ORIENTATION = ShipOrientation

    def __init__(self, size: ShipSize, bow_location: Dot, orientation: ShipOrientation):
        self.size = size
        self.bow_location = bow_location
        self.orientation = orientation
        self.health = self.size.value

    def __str__(self):
        return f"{self.size.name.capitalize()} ship, {self.orientation.name} orientation: {self.dots}."

    @property
    def dots(self) -> list:
        """ Получить точки в которых находится корабль. """
        ship_dots = []
        for n in range(self.size.value):
            if self.orientation == ShipOrientation.vertical:
                dot = Dot(x=self.bow_location.x, y=self.bow_location.y + n)
            else:
                dot = Dot(x=self.bow_location.x + n, y=self.bow_location.y)
            ship_dots.append(dot)
        return ship_dots

    def is_alive(self) -> bool:
        """ Жив ли корабль. """
        return self.health > 0

    def is_hit(self, shot: Dot) -> bool:
        """ Попал ли выстрел по кораблю. """
        return shot in self.dots


if __name__ == "__main__":
    pass

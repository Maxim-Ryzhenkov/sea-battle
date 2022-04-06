import enum


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


class Dot:
    """
        Точка игрового поля
    """
    def __init__(self, vertical_coord: Letter, horizontal_coord: int):
        self.vertical_coord = vertical_coord
        self.horizontal_coord = horizontal_coord

    def __repr__(self):
        return f"Dot {self.vertical_coord}: {self.horizontal_coord}"


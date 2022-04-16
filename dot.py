class Dot:
    """
        Точка игрового поля.
    """

    def __init__(self, x: int, y: int):
        """
        :param x: Горизонтальная координата.
        :param y: Вертикальная координата.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

    def __eq__(self, other):
        """ Сравнить две точки между собой. """
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    pass

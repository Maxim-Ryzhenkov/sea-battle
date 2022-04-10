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
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    dot_1 = Dot(2, 3)
    dot_2 = Dot(2, 3)
    dot_3 = Dot(3, 2)
    print(dot_1)
    print(dot_2)
    print(dot_3)
    print(dot_1 == dot_2)
    print(dot_1 == dot_3)

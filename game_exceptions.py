# coding: utf-8

"""
В модуле определены кастомные классы исключений для игры 'Морской бой'.
"""


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Точка находится за пределами игрового поля."


class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку."


class BoardWrongShipException(BoardException):
    pass

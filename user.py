from game_field import GameField


class Player:
    pass


class AI(Player):
    pass


class User(Player):
    """
        Класс описывает пользователя
    """
    def __init__(self, name):
        self.name = name
        self.game_field = GameField(6)

    def has_alive_ships(self):
        """  """
        pass

    def strike(self, vertical_coord: int, horizontal_coord: int, other_user):
        """ Сделать выстрел. """
        pass



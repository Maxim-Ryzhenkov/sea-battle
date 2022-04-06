import os
import time
import enum
from dot import Dot


CURSOR_SIGN = "?"
EXIT_KEY = "q"
ARROWS = ["a", "s", "w", "d"]

MESSAGE = f"""{'=' * 60}
Выход из игры - "{EXIT_KEY}"
Поставить крестик или нолик в свой ход -"Пробел"
Перемещайте курсор стрелками         W(вверх)
                            A(влево) S(вниз) D(вправо)
(Нажатие каждой клавиши завершается нажатием 'Enter')
{'=' * 60}
"""


def exit_game():
    print("Игра прервана пользователем!")
    exit(0)


if __name__ == "__main__":

    user = User("Maksim")
    user.battle_field.render()


    # print("Игра в крестики-нолики.")
    # PLAYER_1['name'] = input("Введите имя первого игрока (играет крестиками): ")
    # PLAYER_2['name'] = input("Введите имя второго игрока (играет ноликами): ")


    # while True:
    #     # Цикл игры
    #     while True:
    #         # Цикл хода игрока
    #         os.system('cls')
    #         print(MESSAGE)
    #         print(f"Сейчас ходит {CURRENT_PLAYER['name']}. Поставьте '{CURRENT_PLAYER['sign']}' в свободной клетке.")
    #         render_field(render_cursor=True)
    #
    #         # Игрок нажимает клавишу-команду + 'Enter'
    #         command = input().lower()
    #
    #         if command in ARROWS:
    #             # Игрок перемещает курсор
    #             print(f"Нажата стрелка '{command}'")
    #             move_cursor(arrow=command)
    #
    #         elif command == EXIT_KEY:
    #             # Игрок прерывает игру
    #             exit_game()
    #
    #         elif command == " " or command == CURRENT_PLAYER["sign"]:
    #             # Игрок ставит крестик или нолик на поле
    #             if get_cursor_position_value() != FREE_SIGN:
    #                 print(f"Сделать ход можно только на свободной клетке! ")
    #                 render_field(render_cursor=False)
    #                 time.sleep(3)
    #                 continue
    #
    #             set_cursor_position_value(CURRENT_PLAYER["sign"])
    #             if is_player_win():
    #                 # Если игрок выиграл - игра завершается
    #                 print(f"{CURRENT_PLAYER['name']} выиграл! Игра окончена.")
    #                 render_field(render_cursor=False)
    #                 exit(0)
    #
    #             # Если не выиграл
    #             free_position = get_first_free_position(GAME_FIELD)
    #             if not free_position:
    #                 print("Игра закончена, потому что все ходы исчерпаны! Кажется у нас ничья!")
    #                 exit(0)
    #             # Установить курсор на свободную клетку поля и передать ход другому игроку
    #             row, column = free_position
    #             set_cursor_position(row_number=row, column_number=column)
    #             CURRENT_PLAYER = switch_player()
    #             break
    #         else:
    #             print(f"Получена неизвествная клавиша-команда '{command}'. \n"
    #                   f"Используйте команды, указанные в подсказке к игре.")
    #             time.sleep(3)
    #             continue

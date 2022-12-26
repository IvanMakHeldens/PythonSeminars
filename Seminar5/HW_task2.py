# Создайте программу для игры в ""Крестики-нолики"".

import random
import time
# player_name = input("Как звать? Введите имя: ")

# if cur_player == 0:
#     print(f"{player_name}, ХАДИ!")

def generate_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(' ')
    return board

def print_board(board):
    for i in range(len(board)):
        print(' | '.join(board[i]))
        if i != len(board) - 1:
            print('-' * (len(board) * 4 - 3))



def check_position(position, board):
    if not (0 <= position[0] < len(board) or 0 <= position[1] < len(board[0])):
        return False
    else:
        return board[position[0]][position[1]] == ' '

def check_board_full(board):
    for i in range(len(board)):
        for j in board[i]:
            if j == ' ':
                return False
    return True


def check_win(board):
    for i in board:
        if i.count('X') == len(board) or i.count('0') == len(board):
            return True
    for i in range(len(board)):
        col = [board[j][i] for j in range(len(board))]
        if col.count('X') == len(board) or col.count('0') == len(board):
            return True
    diag1 = [board[i][i] for i in range(len(board))]
    if diag1.count('X') == len(board) or diag1.count('0') == len(board):
        return True
    diag2 =  [board[i][-i -1] for i in range(len(board))]
    if diag2.count('X') == len(board) or diag2.count('0') == len(board):
        return True
    return False

def player_turn(board):
    position = [-1, -1]
    while not check_position(position, board):
        position = [int(input(f'Ваш ход. Введите номер строки (1-{len(board)}): ')) -1,
                    int(input(f'Введите номер столбца (1-{len(board)}): ')) -1]
        if not check_position(position, board):
            print('Неверная позиция. Попробуйте снова')
            time.sleep(0.5)
    return position

def bot_turn(board):
    print('Ходит бот')
    time.sleep(0.5)
    position = [-1, -1]
    while not check_position(position, board):
        position = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) -1)]
    return position

def play_game(board):
    cur_player = random.randint(0, 1)
    while not check_board_full(board):
        if cur_player == 0:
            position = player_turn(board)
        else:
            position = bot_turn(board)
        board[position[0]][position[1]] = 'X' if cur_player else '0'
        print_board(board)
        print()
        if check_win(board):
            print(f'Игра завершена. {"Вы выиграли!" if cur_player == 0 else "Выиграл бот"}')
            break
        if cur_player == 0:
            cur_player = 1
        else:
            cur_player = 0
    else:
        print('Никто не выиграл')

board_sizee = 3

play_game(generate_board(board_sizee))

    



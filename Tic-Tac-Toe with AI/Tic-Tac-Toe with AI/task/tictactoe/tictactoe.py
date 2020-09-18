# write your code here
import random


def print_field(game_field):
    print('---------')
    for i in range(3):
        print_str = []
        for j in range(3):
            temp_chr = game_field[i * 3 + j]
            if temp_chr == '_':
                print_str.append(' ')
            else:
                print_str.append(temp_chr)
        print('| {} {} {} |'.format(print_str[0], print_str[1], print_str[2]))
    print('---------')


def is_game_finished(game_field):
    if game_field[0] == game_field[1] == game_field[2] != '_':
        print('{} wins'.format(game_field[0]))
        return True
    elif game_field[3] == game_field[4] == game_field[5] != '_':
        print('{} wins'.format(game_field[3]))
        return True
    elif game_field[6] == game_field[7] == game_field[8] != '_':
        print('{} wins'.format(game_field[6]))
        return True
    elif game_field[0] == game_field[3] == game_field[6] != '_':
        print('{} wins'.format(game_field[0]))
        return True
    elif game_field[1] == game_field[4] == game_field[7] != '_':
        print('{} wins'.format(game_field[1]))
        return True
    elif game_field[2] == game_field[5] == game_field[8] != '_':
        print('{} wins'.format(game_field[2]))
        return True
    elif game_field[0] == game_field[4] == game_field[8] != '_':
        print('{} wins'.format(game_field[0]))
        return True
    elif game_field[2] == game_field[4] == game_field[6] != '_':
        print('{} wins'.format(game_field[2]))
        return True
    elif '_' not in game_field:
        print('Draw')
        return True
    else:
        return False


def user_turn(game_field):
    while True:
        coordinates_str = input('Enter the coordinates: ')
        coordinates_lst = coordinates_str.split()
        try:
            i = int(coordinates_lst[0]) - 1
            j = int(coordinates_lst[1]) - 1
            if i > 2 or i < 0 or j > 2 or j < 0:
                print('Coordinates should be from 1 to 3!')
                continue
            else:
                element_index = (2 - j) * 3 + i
                if game_field[element_index] != '_':
                    print('This cell is occupied! Choose another one!')
                    continue
                else:
                    x_count = game_field.count('X')
                    o_count = game_field.count('O')
                    symbol = 'X' if x_count == o_count else 'O'
                    result = game_field[0:element_index] + symbol + game_field[element_index + 1::]
                    return result
        except ValueError:
            print('You should enter numbers!')
            continue
        except IndexError:
            print('You should enter numbers!')
            continue


def ai_easy_turn(game_field):
    print('Making move level "easy"')
    empty_indexes = [x for x in range(len(game_field)) if game_field[x] == '_']
    ai_choose = random.choice(empty_indexes)
    x_count = game_field.count('X')
    o_count = game_field.count('O')
    symbol = 'X' if x_count == o_count else 'O'
    result = game_field[0:ai_choose] + symbol + game_field[ai_choose + 1::]
    return result


def ai_medium_turn(game_field):
    print('Making move level "medium"')
    x_count = game_field.count('X')
    o_count = game_field.count('O')
    symbol = 'X' if x_count == o_count else 'O'
    if game_field[0] != '_' and game_field[0] == game_field[1] and game_field[2] == '_':
        result = game_field[0:2] + symbol + game_field[2 + 1::]
        return result
    elif game_field[0] != '_' and game_field[0] == game_field[2] and game_field[1] == '_':
        result = game_field[0:1] + symbol + game_field[1 + 1::]
        return result
    elif game_field[1] != '_' and game_field[1] == game_field[2] and game_field[0] == '_':
        result = game_field[0:0] + symbol + game_field[0 + 1::]
        return result
    elif game_field[3] != '_' and game_field[3] == game_field[4] and game_field[5] == '_':
        result = game_field[0:5] + symbol + game_field[5 + 1::]
        return result
    elif game_field[3] != '_' and game_field[3] == game_field[5] and game_field[4] == '_':
        result = game_field[0:4] + symbol + game_field[4 + 1::]
        return result
    elif game_field[4] != '_' and game_field[4] == game_field[5] and game_field[3] == '_':
        result = game_field[0:3] + symbol + game_field[3 + 1::]
        return result
    elif game_field[6] != '_' and game_field[6] == game_field[7] and game_field[8] == '_':
        result = game_field[0:8] + symbol + game_field[8 + 1::]
        return result
    elif game_field[6] != '_' and game_field[6] == game_field[8] and game_field[7] == '_':
        result = game_field[0:7] + symbol + game_field[7 + 1::]
        return result
    elif game_field[7] != '_' and game_field[7] == game_field[8] and game_field[6] == '_':
        result = game_field[0:6] + symbol + game_field[6 + 1::]
        return result
    elif game_field[0] != '_' and game_field[0] == game_field[3] and game_field[6] == '_':
        result = game_field[0:6] + symbol + game_field[6 + 1::]
        return result
    elif game_field[0] != '_' and game_field[0] == game_field[6] and game_field[3] == '_':
        result = game_field[0:3] + symbol + game_field[3 + 1::]
        return result
    elif game_field[3] != '_' and game_field[3] == game_field[6] and game_field[0] == '_':
        result = game_field[0:0] + symbol + game_field[0 + 1::]
        return result
    elif game_field[1] != '_' and game_field[1] == game_field[4] and game_field[7] == '_':
        result = game_field[0:7] + symbol + game_field[7 + 1::]
        return result
    elif game_field[1] != '_' and game_field[1] == game_field[7] and game_field[4] == '_':
        result = game_field[0:4] + symbol + game_field[4 + 1::]
        return result
    elif game_field[4] != '_' and game_field[4] == game_field[7] and game_field[1] == '_':
        result = game_field[0:1] + symbol + game_field[1 + 1::]
        return result
    elif game_field[2] != '_' and game_field[2] == game_field[5] and game_field[8] == '_':
        result = game_field[0:8] + symbol + game_field[8 + 1::]
        return result
    elif game_field[2] != '_' and game_field[2] == game_field[8] and game_field[5] == '_':
        result = game_field[0:5] + symbol + game_field[5 + 1::]
        return result
    elif game_field[5] != '_' and game_field[5] == game_field[8] and game_field[2] == '_':
        result = game_field[0:2] + symbol + game_field[2 + 1::]
        return result
    elif game_field[0] != '_' and game_field[0] == game_field[4] and game_field[8] == '_':
        result = game_field[0:8] + symbol + game_field[8 + 1::]
        return result
    elif game_field[0] != '_' and game_field[0] == game_field[8] and game_field[4] == '_':
        result = game_field[0:4] + symbol + game_field[4 + 1::]
        return result
    elif game_field[4] != '_' and game_field[4] == game_field[8] and game_field[0] == '_':
        result = game_field[0:0] + symbol + game_field[0 + 1::]
        return result
    elif game_field[2] != '_' and game_field[2] == game_field[4] and game_field[6] == '_':
        result = game_field[0:6] + symbol + game_field[6 + 1::]
        return result
    elif game_field[2] != '_' and game_field[2] == game_field[6] and game_field[4] == '_':
        result = game_field[0:4] + symbol + game_field[4 + 1::]
        return result
    elif game_field[4] != '_' and game_field[4] == game_field[6] and game_field[2] == '_':
        result = game_field[0:2] + symbol + game_field[2 + 1::]
        return result
    else:
        empty_indexes = [x for x in range(len(game_field)) if game_field[x] == '_']
        ai_choose = random.choice(empty_indexes)
        result = game_field[0:ai_choose] + symbol + game_field[ai_choose + 1::]
        return result


def ai_hard_turn(game_field):
    print('Making move level "hard"')
    x_count = game_field.count('X')
    o_count = game_field.count('O')
    symbol = 'X' if x_count == o_count else 'O'
    return tictac(game_field, symbol)


def wins(grid):
    rows = [[grid[i+j] for j in range(3)] for i in range(0, 7, 3)]
    cols = [[grid[i+j] for j in range(0, 7, 3)] for i in range(3)]
    digs = [[grid[i] for i in range(0, 9, 4)], [grid[i] for i in range(2, 7, 2)]]
    return any(all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row) for row in rows + cols + digs)


def full(grid):
    return all(cell == 'X' or cell == 'O' for cell in grid)


def move(grid, cell, symbol):
    moved = list(grid)
    moved[cell] = symbol
    return moved


def moves(grid, symbol):
    return [move(grid, cell, symbol) for cell in range(9) if grid[cell] not in ('X', 'O')]


def minimax(grid, symbol):
    if wins(grid):
        return (1 if symbol == 'O' else -1), None
    elif full(grid):
        return 0, None
    elif symbol == 'X':
        best_score = -2
        best_move = None
        for move in moves(grid, 'X'):
            score, mv = minimax(move, 'O')
            if score >= best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    elif symbol == 'O':
        best_score = 2
        best_move = None
        for move in moves(grid, 'O'):
            score, mv = minimax(move, 'X')
            if score <= best_score:
                best_score = score
                best_move = move
        return best_score, best_move


def tictac(grid, turn):
    score, mv = minimax(grid, turn)
    return ''.join(mv)


def game_process(gamer1, gamer2):
    field = '_________'
    # print_field(field)
    first_turn = True
    while not is_game_finished(field):
        if first_turn:
            if gamer1 == 'user':
                field = user_turn(field)
            elif gamer1 == 'easy':
                field = ai_easy_turn(field)
            elif gamer1 == 'medium':
                field = ai_medium_turn(field)
            elif gamer1 == 'hard':
                field = ai_hard_turn(field)
        else:
            if gamer2 == 'user':
                field = user_turn(field)
            elif gamer2 == 'easy':
                field = ai_easy_turn(field)
            elif gamer2 == 'medium':
                field = ai_medium_turn(field)
            elif gamer2 == 'hard':
                field = ai_hard_turn(field)
        first_turn = not first_turn
        print_field(field)


while True:
    command = input('Input command: ')
    if command == 'exit':
        break
    else:
        command_lst = command.split()
        if len(command_lst) != 3:
            print('Bad parameters!')
            continue
        else:
            if command_lst[0] != 'start':
                print('Bad parameters!')
                continue
            elif command_lst[1] != 'easy' and command_lst[1] != 'user'\
                    and command_lst[1] != 'medium' and command_lst[1] != 'hard':
                print('Bad parameters!')
                continue
            elif command_lst[2] != 'easy' and command_lst[2] != 'user'\
                    and command_lst[2] != 'medium' and command_lst[2] != 'hard':
                print('Bad parameters!')
                continue
            else:
                game_process(command_lst[1], command_lst[2])
                print()

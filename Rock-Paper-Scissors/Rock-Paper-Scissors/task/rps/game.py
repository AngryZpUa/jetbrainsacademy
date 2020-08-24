# Write your code here
import random


def get_rating_dict():
    result = dict()
    rating_file = open('rating.txt')
    for rating_str in rating_file:
        split_str = rating_str.split()
        result.update({split_str[0]: int(split_str[1])})
    rating_file.close()
    return result


def save_rating_dict(rating_to_save):
    rating_file = open('rating.txt', 'w')
    for item in rating_to_save:
        rating_file.write('{} {}\n'.format(item[0], item[1]))
    rating_file.close()


def is_user_win(user, computer):
    options_list = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
                    'dragon', 'devil', 'lightning', 'gun']
    new_list = options_list * 2
    winners = new_list[new_list.index(computer) + 1:new_list.index(computer) + 8:]
    return user not in winners


lose_str = 'Sorry, but the computer chose {}'
draw_str = 'There is a draw ({})'
win_str = 'Well done. The computer chose {} and failed'
print('Enter your name:')
player_name = input()
print('Hello, {}'.format(player_name))
rating = get_rating_dict()
rating_value = rating.get(player_name, 0)
game_mode = input()
if game_mode == '':
    list_of_options = ['rock', 'paper', 'scissors']
else:
    list_of_options = game_mode.split(',')
print("Okay, let's start")
while True:
    user_choose = input()
    computer_choose = random.choice(list_of_options)
    if user_choose == '!exit':
        print('Bye!')
        rating.update({player_name: rating_value})
        save_rating_dict(rating)
        break
    elif user_choose == '!rating':
        print('Your rating: {}'.format(rating_value))
    elif user_choose in list_of_options:
        if user_choose == computer_choose:
            rating_value += 50
            print(draw_str.format(computer_choose))
        elif is_user_win(user_choose, computer_choose):
            rating_value += 100
            print(win_str.format(computer_choose))
        else:
            print(lose_str.format(computer_choose))
    else:
        print('Invalid input')

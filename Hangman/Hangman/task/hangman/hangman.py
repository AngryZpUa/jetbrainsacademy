# Write your code here
import random


def game():
    words = ('python', 'java', 'kotlin', 'javascript')
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z')
    lives = 8
    word = random.choice(words)
    letters = set()
    all_input = set()
    while lives > 0:
        print()
        secret_word = word
        for i in word:
            if i not in letters:
                secret_word = str(secret_word).replace(i, '-', len(word))
        print(secret_word)
        new_char = input('Input a letter: ')
        if len(new_char) != 1:
            print('You should input a single letter')
        elif new_char not in alphabet:
            print('It is not an ASCII lowercase letter')
        else:
            if new_char in all_input:
                print('You already typed this letter')
            elif new_char in word and new_char not in letters:
                letters.add(new_char)
                all_input.add(new_char)
                if set(word) == letters:
                    print()
                    print(word)
                    print('You guessed the word!')
                    print('You survived!')
                    break
            else:
                print('No such letter in the word')
                lives -= 1
            all_input.add(new_char)
    if lives == 0:
        print('You are hanged!')


print('H A N G M A N')
print('Type "play" to play the game, "exit" to quit:')
player_choice = input()
while True:
    if player_choice == 'play':
        game()
    if player_choice == 'exit':
        break
    print()
    print('Type "play" to play the game, "exit" to quit:')
    player_choice = input()

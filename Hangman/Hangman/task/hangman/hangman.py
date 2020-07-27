# Write your code here
import random


words = ('python', 'java', 'kotlin', 'javascript')
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')
print('H A N G M A N')
lives = 8
word = random.choice(words)
#output_string = 'Guess the word ' + word[0:3].ljust(len(word), '-') + ': '
#if word == input(output_string):
#    print('You survived!')
#else:
#    print('You are hanged!')
letters = set()
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
    elif new_char in word and new_char not in letters:
        letters.add(new_char)
        if set(word) == letters:
            print()
            print(word)
            print('You guessed the word!')
            print('You survived!')
            break
    elif new_char in word and new_char in letters:
        print('You already typed this letter')
    elif new_char in alphabet:
        print('No such letter in the word')
        lives -= 1
    else:
        print('It is not an ASCII lowercase letter')
if lives == 0:
    print('You are hanged!')

# Write your code here
import random


words = ('python', 'java', 'kotlin', 'javascript')
print('H A N G M A N')
word = random.choice(words)
#output_string = 'Guess the word ' + word[0:3].ljust(len(word), '-') + ': '
#if word == input(output_string):
#    print('You survived!')
#else:
#    print('You are hanged!')
letters = set()
for _ in range(8):
    print()
    secret_word = word
    for i in word:
        if i not in letters:
            secret_word = str(secret_word).replace(i, '-', len(word))
    print(secret_word)
    new_char = input('Input a letter: ')
    if new_char in word:
        letters.add(new_char)
    else:
        print('No such letter in the word')
print()
print('Thanks for playing!')
print("We'll see how well you did in the next stage")

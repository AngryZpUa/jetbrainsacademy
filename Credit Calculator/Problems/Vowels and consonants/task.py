list_vowels = ['a', 'e', 'i', 'o', 'u']
list_consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
string = input()
for i in string:
    if i in list_vowels:
        print('vowel')
    elif i in list_consonant:
        print('consonant')
    else:
        break

string = input()
for char in string:
    if char.isupper():
        string = string.replace(char, "_" + char.lower())
print(string)

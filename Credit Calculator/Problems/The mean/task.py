string = input()
total = 0
count = 0
while string != '.':
    total += int(string)
    count += 1
    string = input()
print(total / count)

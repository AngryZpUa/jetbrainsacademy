N = int(input())
counter = 1
factorial = 1
while counter <= N:
    factorial *= counter
    counter += 1
print(factorial)

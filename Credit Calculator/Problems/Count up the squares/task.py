# put your python code here

first_integer = int(input())
total = first_integer
total_squares = first_integer ** 2
while total != 0:
    next_integer = int(input())
    total += next_integer
    total_squares += next_integer ** 2
print(total_squares)

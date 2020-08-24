# read sums.txt
my_file = open('sums.txt')
lines = my_file.readlines()
for line in lines:
    numbers = line.split(' ')
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    summa = number1 + number2
    print(summa)
my_file.close()

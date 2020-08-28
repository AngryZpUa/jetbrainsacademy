def range_sum(numbers, start, end):
    summa = 0
    for number in numbers:
        if start <= number <= end:
            summa += number
    return summa


input_numbers = [int(x) for x in input().split()]
params = input().split()
a, b = int(params[0]), int(params[1])
print(range_sum(input_numbers, a, b))

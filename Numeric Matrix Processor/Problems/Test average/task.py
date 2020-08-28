def average_mark(*arguments):
    count = 0
    summa = 0
    my_args = [int(x) for x in arguments]
    for argument in my_args:
        summa += argument
        count += 1
    return round(summa / count, 1)

n = int(input())


def squares(k):
    for i in range(k):
        yield (i + 1) ** 2


# Don't forget to print out the first n numbers one by one here
my_generator = squares(n)
for _ in range(n):
    print(next(my_generator))

n = int(input())


def even(k):
    for i in range(k):
        yield i * 2


# Don't forget to print out the first n numbers one by one here
my_generator = even(n)
for _ in range(n):
    print(next(my_generator))

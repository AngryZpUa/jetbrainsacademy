def fibonacci(n):
    my_lst = []
    while len(my_lst) < n:
        if len(my_lst) == 0:
            tmp = 0
            my_lst.append(tmp)
            yield tmp
        elif len(my_lst) == 1:
            tmp = 1
            my_lst.append(tmp)
            yield tmp
        else:
            tmp = my_lst[len(my_lst) - 1] + my_lst[len(my_lst) - 2]
            my_lst.append(tmp)
            yield tmp

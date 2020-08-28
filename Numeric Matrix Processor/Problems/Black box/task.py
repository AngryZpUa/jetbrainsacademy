# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = blackbox(my_list)
if new_list is my_list:
    print('modifies')
else:
    print('new')

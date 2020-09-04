# write your code here
try:
    hash(some_object)
except TypeError:
    print('Not hashable')
else:
    print('Hashable')

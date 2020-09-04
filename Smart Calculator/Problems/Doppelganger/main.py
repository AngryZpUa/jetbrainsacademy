# the object_list has already been defined
# write your code here
count = 0
for obj in object_list:
    if object_list.count(obj) > 1:
        try:
            hash(obj)
            count += 1
        except TypeError:
            pass
print(count)

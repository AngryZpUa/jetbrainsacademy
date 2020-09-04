# create your dictionary here
objects_dict = {}
for obj in objects:
    try:
        object_hash = hash(obj)
        objects_dict[obj] = object_hash
    except TypeError:
        pass

def find_my_list(lists, my_list):
    for list_index, lst in enumerate(lists):
        if id(lst) == id(my_list):
            return list_index
    return None

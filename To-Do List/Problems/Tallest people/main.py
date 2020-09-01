def tallest_people(**kwargs):
    result_dict = {}
    max_height = None
    for key, value in kwargs.items():
        if max_height is None:
            max_height = value
            result_dict[key] = value
        elif max_height == value:
            result_dict[key] = value
        elif max_height < value:
            max_height = value
            result_dict = {key: value}
    for key, value in sorted(result_dict.items()):
        print('{} : {}'.format(key, value))

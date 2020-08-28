def last_indexof_max(numbers):
    # write the modified algorithm here
    index = 0
    max_value = numbers[index]
    for i in range(1, len(numbers)):
        if numbers[i] >= max_value:
            max_value = numbers[i]
            index = i
    return index

def startswith_capital_counter(names):
    result = 0
    for name in names:
        if name.capitalize() == name:
            result += 1
    return result

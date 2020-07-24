def get_percentage(number, precision=None):
    result = round(number * 100, precision)
    return str(result) + '%'

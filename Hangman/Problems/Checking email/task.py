def check_email(string):
    if ' ' in string:
        return False
    if '@' not in string:
        return False
    if string.find('.', string.find('@')) == -1:
        return False
    if string.find('@') + 1 == string.find('.'):
        return False
    return True

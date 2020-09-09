# put your python code here

def check_brackets(check_str):
    lst = []
    for symbol in check_str:
        if symbol == '(':
            lst.append(symbol)
        elif symbol == ')':
            try:
                lst.pop()
            except IndexError:
                return False
    return len(lst) == 0


input_str = input()
result = check_brackets(input_str)
if result:
    print('OK')
else:
    print('ERROR')

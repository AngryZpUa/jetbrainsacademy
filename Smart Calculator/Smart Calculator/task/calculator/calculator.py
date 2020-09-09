# write your code here
calc_memory = {}


def refactoring(operation, comp_str):
    result = None
    symbol = None
    if operation == '^':
        symbol = comp_str.index('^')
    elif operation == '*':
        symbol = comp_str.index('*')
    elif operation == '/':
        symbol = comp_str.index('/')
    start = 0
    end = 0
    for i in range(symbol + 1, len(comp_str)):
        if comp_str[i].isdigit():
            end = i
        else:
            break
    for i in range(symbol - 1, -1, -1):
        if comp_str[i].isdigit():
            start = i
        else:
            break
    if operation == '^':
        base = comp_str[start: symbol]
        power = comp_str[symbol + 1: end + 1]
        result = pow(int(base), int(power))
    elif operation == '*':
        num1 = comp_str[start: symbol]
        num2 = comp_str[symbol + 1: end + 1]
        result = int(num1) * int(num2)
    elif operation == '/':
        num1 = comp_str[start: symbol]
        num2 = comp_str[symbol + 1: end + 1]
        result = int(num1) // int(num2)
    return compute(comp_str[0: start] + str(result) + comp_str[end + 1:])


def compute(compute_str):
    if '(' in compute_str and ')' in compute_str:
        start = 0
        for i in range(len(compute_str)):
            if compute_str[i] == '(':
                start = i
        end = 0
        for i in range(start, len(compute_str)):
            if compute_str[i] == ')':
                end = i
                break
        return compute(compute_str[0: start] + str(compute(compute_str[start + 1: end])) + compute_str[end+1:])
    elif '^' in compute_str:
        return refactoring('^', compute_str)
    elif '*' in compute_str:
        return refactoring('*', compute_str)
    elif '/' in compute_str:
        return refactoring('/', compute_str)
    elif '+' in compute_str or '-' in compute_str:
        return sum_numbers(split_str_to_ints(compute_str))
    else:
        return int(compute_str)


def normalize_input(my_str):
    while '++' in my_str or '--' in my_str or '+-' in my_str or '-+' in my_str:
        if '++' in my_str:
            my_str = my_str.replace('++', '+')
        elif '--' in my_str:
            my_str = my_str.replace('--', '+')
        elif '+-' in my_str:
            my_str = my_str.replace('+-', '-')
        elif '-+' in my_str:
            my_str = my_str.replace('-+', '-')
    return my_str


def sum_numbers(numbers):
    summa = 0
    for num in numbers:
        summa += num
    return summa


def split_str_to_ints(str_to_nums):
    result_list = []
    int_str = ''
    for i in range(len(str_to_nums)):
        if str_to_nums[i] in '-+' and int_str != '':
            result_list.append(int(int_str))
            int_str = str_to_nums[i]
        else:
            int_str += str_to_nums[i]
    result_list.append(int(int_str))
    return result_list


def check_brackets(check_str):
    if '(' in check_str and ')' not in check_str:
        return False
    elif '(' not in check_str and ')' in check_str:
        return False
    elif '(' not in check_str and ')' not in check_str:
        return True
    else:
        start = 0
        end = 0
        for i in range(len(check_str)):
            if check_str[i] == '(':
                start = i
        for i in range(start, len(check_str)):
            if check_str[i] == ')':
                end = i
                break
        if end < start:
            return False
        return check_brackets(check_str[0:start] + check_str[end+1::])


def var_to_value(rep_str):
    try:
        str_val = ''
        temp_str = ''
        for chr1 in rep_str:
            if chr1 in '-+()*/^':
                if temp_str != '':
                    if temp_str.isalpha():
                        str_val += str(calc_memory[temp_str])
                    elif temp_str.isdigit():
                        str_val += temp_str
                    temp_str = ''
                str_val += chr1
            else:
                temp_str += chr1
        if temp_str.isalpha():
            str_val += str(calc_memory[temp_str])
        elif temp_str.isdigit():
            str_val += temp_str
        return str_val
    except KeyError:
        return None


while True:
    input_str = input()
    if input_str.startswith('/'):
        if input_str == '/exit':
            print('Bye!')
            break
        elif input_str == '/help':
            print('The program calculates numbers')
        else:
            print('Unknown command')
    elif input_str == '':
        pass
    else:
        clear_str = input_str.replace(' ', '')
        if '=' in clear_str:
            try:
                variable, value = clear_str.split('=')
                if variable.isalpha():
                    if value in calc_memory.keys():
                        calc_memory[variable] = calc_memory[value]
                    else:
                        if value.isalpha():
                            print('Unknown variable')
                        else:
                            try:
                                int_value = int(value)
                                calc_memory[variable] = int_value
                            except ValueError:
                                print('Invalid assignment')
                else:
                    print('Invalid identifier')
            except ValueError:
                print('Invalid assignment')
        else:
            if '+' not in clear_str and '-' not in clear_str and '*' not in clear_str and '/' not in clear_str \
                    and '^' not in clear_str:
                if clear_str.isalpha():
                    if clear_str in calc_memory.keys():
                        print(calc_memory[clear_str])
                    else:
                        print('Unknown variable')
                else:
                    print('Invalid identifier')
            else:
                if '**' in clear_str or '//' in clear_str or check_brackets(clear_str) is False \
                        or clear_str.startswith('*') or clear_str.startswith('/') or clear_str.startswith('^'):
                    print('Invalid expression')
                else:
                    normal_str = normalize_input(clear_str)
                    replaced_str = var_to_value(normal_str)
                    if replaced_str is not None:
                        print(compute(replaced_str))
                    else:
                        print("Invalid assignment")

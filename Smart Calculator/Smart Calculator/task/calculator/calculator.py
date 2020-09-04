# write your code here

def sum_numbers(numbers):
    summa = 0
    for num in numbers:
        summa += num
    return summa


def normalize_input(dirty_str):
    my_str = dirty_str.replace(' ', '')
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


def check_str_to_possibility(check_str):
    for i in check_str:
        if i not in ' +-1234567890':
            return False
    return True


def split_str_to_ints(str_to_nums):
    ints_list = []
    int_str = ''
    for i in range(len(str_to_nums)):
        if str_to_nums[i] in '-+' and int_str != '':
            ints_list.append(int(int_str))
            int_str = str_to_nums[i]
        else:
            int_str += str_to_nums[i]
    ints_list.append(int(int_str))
    return ints_list


def check_two_nums_with_whitespace(checked_str):
    for i in '0123456789':
        for j in '0123456789':
            temp_str = '{} {}'.format(i, j)
            if temp_str in checked_str:
                return True
    return False


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
        if check_str_to_possibility(input_str):
            if check_two_nums_with_whitespace(input_str):
                print('Invalid expression')
            else:
                normal_str = normalize_input(input_str)
                if normal_str.endswith('+') or normal_str.endswith('-'):
                    print('Invalid expression')
                else:
                    print(sum_numbers(split_str_to_ints(normal_str)))
        else:
            print('Invalid expression')

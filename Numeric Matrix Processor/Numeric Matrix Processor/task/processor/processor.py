def input_matrix_size_and_elements():
    matrix_str_size = input('Enter size of matrix:').split()
    rows = int(matrix_str_size[0])
    column = int(matrix_str_size[1])
    result = []
    for _ in range(rows):
        row = []
        str_elements = input().split()
        for i in range(column):
            row.append(float(str_elements[i]))
        result.append(row)
    return result


def matrix_addition(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print('The operation cannot be performed.')
        print()
        return None
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


def matrix_multiply_number(matrix_a, number):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] * number)
        result.append(row)
    return result


def multiply_matrix(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        print('The operation cannot be performed.')
        print()
        return None
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            summa = 0
            for k in range(len(matrix_b)):
                summa += matrix_a[i][k] * matrix_b[k][j]
            row.append(summa)
        result.append(row)
    return result


def transposition(matrix_a, transposition_type):
    result = []
    if transposition_type == '1':
        for i in range(len(matrix_a)):
            row = []
            for j in range(len(matrix_a[0])):
                row.append(matrix_a[j][i])
            result.append(row)
    elif transposition_type == '2':
        temp_1 = transposition(matrix_a, '3')
        temp_2 = transposition(temp_1, '4')
        result = transposition(temp_2, '1')
    elif transposition_type == '3':
        for i in range(len(matrix_a)):
            row = matrix_a[i]
            result.append(row[::-1])
    elif transposition_type == '4':
        result = matrix_a[::-1]
    return result


def print_matrix(matrix_a):
    print('The result is:')
    for i in range(len(matrix_a)):
        str_line = ''
        for j in range(len(matrix_a[i])):
            str_line += str(matrix_a[i][j]) + ' '
        print(str_line[0:len(str_line)-1])
    print()


while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('0. Exit')
    main_menu_choice = input('Your choice:')
    if main_menu_choice == '0':
        break
    elif main_menu_choice == '1':
        a = input_matrix_size_and_elements()
        b = input_matrix_size_and_elements()
        c = matrix_addition(a, b)
        if c is None:
            continue
        print_matrix(c)
    elif main_menu_choice == '2':
        a = input_matrix_size_and_elements()
        constant = float(input('Enter constant:'))
        c = matrix_multiply_number(a, constant)
        print_matrix(c)
    elif main_menu_choice == '3':
        a = input_matrix_size_and_elements()
        b = input_matrix_size_and_elements()
        c = multiply_matrix(a, b)
        if c is None:
            continue
        print_matrix(c)
    elif main_menu_choice == '4':
        print()
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        transpose_menu_choice = input('Your choice:')
        a = input_matrix_size_and_elements()
        b = transposition(a, transpose_menu_choice)
        print_matrix(b)

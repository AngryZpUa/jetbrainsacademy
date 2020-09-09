n = int(input())
passed_students = []
answer_students = []
for _ in range(n):
    input_str = input()
    if input_str.startswith('READY '):
        answer_students.insert(0, input_str[6:])
    elif input_str == 'EXTRA':
        temp_value = answer_students.pop()
        answer_students.insert(0, temp_value)
    elif input_str == 'PASSED':
        passed_students.append(answer_students.pop())
for student in passed_students:
    print(student)

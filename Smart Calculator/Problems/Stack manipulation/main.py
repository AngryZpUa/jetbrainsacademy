n = int(input())
stack = []
for _ in range(n):
    input_str = input()
    if input_str == 'POP':
        stack.pop()
    else:
        command, value = input_str.split()
        stack.append(int(value))
stack.reverse()
for num in stack:
    print(num)

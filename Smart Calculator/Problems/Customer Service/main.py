from collections import deque

n = int(input())
lst = deque()
for _ in range(n):
    input_str = input()
    if input_str.startswith('ISSUE '):
        lst.append(input_str[6:])
    else:
        lst.popleft()
for element in lst:
    print(element)

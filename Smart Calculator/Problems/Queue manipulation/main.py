from collections import deque

n = int(input())
my_queue = deque()
for _ in range(n):
    input_str = input()
    if input_str.startswith('ENQUEUE '):
        my_queue.append(input_str[8:])
    else:
        my_queue.popleft()
for element in my_queue:
    print(element)

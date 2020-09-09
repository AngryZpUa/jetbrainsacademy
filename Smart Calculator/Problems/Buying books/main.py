n = int(input())
lst1 = []
lst2 = []
for _ in range(n):
    input_str = input()
    if input_str.startswith('BUY'):
        lst1.append(input_str[4:])
    else:
        lst2.append(lst1.pop())
for temp_str in lst2:
    print(temp_str)

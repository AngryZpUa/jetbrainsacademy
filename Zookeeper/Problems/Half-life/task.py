N = int(input())
R = int(input())
days = 0
while N > R:
    days += 1
    N //= 2
print(days * 12)

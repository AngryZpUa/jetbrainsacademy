# put your python code here
num1 = int(input())
num2 = int(input())
total = 0
count = 0
for i in range(num1, num2 + 1):
    if i % 3 == 0:
        total += i
        count += 1
print(total / count)

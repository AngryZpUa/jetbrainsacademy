# put your python code here
num = int(input())
div100 = num // 100
num = num % 100
div10 = num // 10
div1 = num % 10
result = div1 + div10 + div100
print(result)

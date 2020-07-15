import math

a = int(input())
result1 = round(2 * math.sqrt(3) * math.pow(a, 2), 2)
result2 = round((1 / 3) * math.sqrt(2) * math.pow(a, 3), 2)
print("{0} {1}".format(result1, result2))

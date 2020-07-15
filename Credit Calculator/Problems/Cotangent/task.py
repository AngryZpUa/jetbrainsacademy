import math

angle = int(input())
radians = (math.pi / 180) * angle
result = round(1 / math.tan(radians), 10)
print(result)

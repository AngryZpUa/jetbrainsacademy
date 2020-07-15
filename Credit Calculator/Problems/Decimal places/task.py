float_number = float(input())
decimals = int(input())
result = "%." + str(decimals) + "f"
print(result % float_number)

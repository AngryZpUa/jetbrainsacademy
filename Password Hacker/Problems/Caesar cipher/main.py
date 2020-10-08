input_str = input()
result = []
for symbol in input_str:
    result.append(chr(ord(symbol) + 1))
print(''.join(result))

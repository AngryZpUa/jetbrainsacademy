input_str = input()
str_bytes = bytes(input_str, encoding='utf-8')
print(str_bytes[len(str_bytes) - 1])

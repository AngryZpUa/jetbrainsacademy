input_str = input()
key_number = int(input())
key_sum = sum(key_number.to_bytes(2, byteorder='little'))
result = []
for str_chr in input_str:
    result.append(chr(ord(str_chr) + key_sum))
print(''.join(result))

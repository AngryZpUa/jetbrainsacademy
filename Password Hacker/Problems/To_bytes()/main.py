input_int = int(input())
print(sum(input_int.to_bytes(2, byteorder='big')))

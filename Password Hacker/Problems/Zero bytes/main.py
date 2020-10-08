# work with this variable
result_str = ''
for _ in range(5):
    result_str += chr(ord(b'\x00'))
zero_bytes = result_str.encode()

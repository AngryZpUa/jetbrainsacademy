str1 = input()
str2 = input()
result = ''
for chr1, chr2 in zip(str1, str2):
    result += chr1 + '' + chr2
print(result)

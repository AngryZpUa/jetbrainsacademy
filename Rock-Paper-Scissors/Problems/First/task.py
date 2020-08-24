# read test_file.txt
my_file = open('test_file.txt', encoding='utf-16')
counter = 0
for line in my_file:
    print(line)
    break
my_file.close()

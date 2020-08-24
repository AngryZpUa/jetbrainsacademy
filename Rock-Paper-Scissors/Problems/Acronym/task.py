# read test.txt
my_file = open('test.txt')
lines = my_file.readlines()
for line in lines:
    print(line[0])
my_file.close()

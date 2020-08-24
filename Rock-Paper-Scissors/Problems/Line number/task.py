# read sample.txt and print the number of lines
my_file = open('sample.txt')
counter = 0
for _ in my_file:
    counter += 1
my_file.close()
print(counter)

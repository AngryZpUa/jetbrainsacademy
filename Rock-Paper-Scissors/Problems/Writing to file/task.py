f_name = "test.txt"
my_string = "A string to be written to a file!"
file_to_write = open(f_name, 'w')
# what to do with the file and the string
print(my_string, file=file_to_write)
file_to_write.close()

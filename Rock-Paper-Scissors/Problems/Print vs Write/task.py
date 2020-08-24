numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_to_write = open('file_with_list.txt', 'w')
file_to_write.write(str(numbers))
file_to_write.close()

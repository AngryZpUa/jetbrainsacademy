# write your code here
for i in range(1, 11):
    with open('file{}.txt'.format(i), 'w') as file_to_write:
        file_to_write.write('{}'.format(i))

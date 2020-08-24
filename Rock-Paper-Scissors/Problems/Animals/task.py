# read animals.txt
# and write animals_new.txt
old_file = open('animals.txt')
animals = old_file.read()
old_file.close()
new_file = open('animals_new.txt', 'w')
animals = animals.replace('\n', ' ')
new_file.write(animals)
new_file.close()

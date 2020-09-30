with open('full_name.txt', 'w') as f3:
    with open('name.txt') as f1:
        with open('surname.txt') as f2:
            name = f1.read()
            surname = f2.read()
            full_name = name + ' ' + surname
            f3.write(full_name)

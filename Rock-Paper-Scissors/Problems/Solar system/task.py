# create the planets.txt
my_file = open('planets.txt', 'w', encoding='utf-8')
planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune']
my_file.writelines(planets)
my_file.close()

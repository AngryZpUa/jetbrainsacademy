class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def print_phrase(self):
        print('"{0}" by {1} ({2}) hangs in the Louvre.'.format(self.title, self.artist, self.year))


name = input()
author = input()
picture_year = int(input())
painting = Painting(name, author, picture_year)
painting.print_phrase()

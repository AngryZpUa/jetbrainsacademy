import math


class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def dist(self, point):
        return math.sqrt(pow(self.x1 - point.x1, 2) + pow(self.y1 - point.y1, 2))

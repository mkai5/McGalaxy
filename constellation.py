import math
import numpy
import matplotlib.pyplot as plt

class Constellation:

    def __init__(self, coordinates):
        coords = coordinates
        shifted = self.shift(coords)
        oriented = self.reorient(shifted)
        self.coords = self.flip(oriented)
        self.second = (self.coords[0][0],self.coords[1][1])
        self.stretch = self.second[1]

        
    def flip(self, coordinates):
        if coordinates[1][0] < 0:
            flipped = []
            for coordinate in coordinates:
                x,y = coordinate
                flipped.append((-x,y))
                return flipped
        else:
            return coordinates


    def span(self,coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dist = math.sqrt((x1-x2)^2 + (y1-y2)^2)
        return dist


    def shift(self,coordinates):
        x, y = coordinates[1]
        shifted = []
        for coordinate in coordinates:
            shifted.append((coordinate[0]-x, coordinate[1]-y))

        return shifted


    
    def reorient(self,coordinates):
        x, y = coordinates[0]
        theta = -math.atan(y/x)
        rotated = []
        for coordinate in coordinates:
            x1 = coordinate[0]
            y1 = coordinate[1]

            x2 = (math.cos(theta) * x1) + (-math.sin(theta) * y1)
            y2 = (math.sin(theta) * x1) + (math.cos(theta) * y1)

            rotated.append((x2,y2))

        return rotated

    def plot(self):
        xs = []
        ys = []
        points = self.coords
        for point in points:
            xs.append(point[0])
            ys.append(point[1])

        plt.plot(xs, ys, 'ro')
        plt.show()





    
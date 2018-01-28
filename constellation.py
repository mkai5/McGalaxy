import math

class Constellation:
    def __init__(self, coordinates):
        self.coords = coordinates
    def reorient(self):
        init_coord_x, init_coord_y = self.coords[0]
        x_change = init_coord_x * -1
        y_change = init_coord_y * -1
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] + x_change, self.coords[i][1] + y_change)
    def span(self):
        init_x, init_y = self.coords[0]
        dist = [math.sqrt((x-init_x)^2 + (y-init_y)^2) for x, y in self.coords]
        return max(dist)

import star

class Constellation:

    def __init__(self, stars):
        self.stars = stars
        self.size = len(stars)

    def get_centroid(self):
        x=0
        y=0
        for i in self.stars:
            x = x + i.coordinates[0]
            y = y + i.coordinates[1]
        size=len(self.stars)
        x = x / size
        y = y / size
        return (x,y)


        
    




    
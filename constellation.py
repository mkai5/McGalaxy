import star

class Constellation:

    constellations = ["Big_Dipper","Aquila"]

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

    def constellation_lookup(s,star_data):
        if (s=="Big_Dipper"):
            con_data= star_data.loc[(star_data["Proper name"] == "Alioth")
            | (star_data["Proper name"] == "Dubhe")
            | (star_data["Proper name"] == "Merak")
            | (star_data["Proper name"] == "Alkaid")
            | (star_data["Proper name"] == "Phad")
            | (star_data["Proper name"] == "Megrez")
            | (star_data["Proper name"] == "Mizar")]
        elif (s=="Aquila"):
            con_data= star_data.loc[(star_data["Proper name"] == "Altair")
            | (star_data["Proper name"] == "Alshain")
            | (star_data["Proper name"] == "Tarazed")]
        else:
            raise ValueError("Constellation not included in lookup function")
        return con_data


        
    




    
import pandas as pd
import numpy as np
import star
import constellation

# Import all McDonalds data
McDs_data = pd.read_csv("Mcdonalds_USA_CAN.csv", encoding="latin-1",
	names = ["Longitude","Latitude","City","Information"])

#Import coordinate positions of star data
star_data = pd.read_csv("hygdata_v3.csv", usecols=["Proper name","x","y","z"])
#Drop all non-named stars
star_data = star_data.dropna()
#Create star instances from star data
star_data=star_data.apply(
	lambda i: star.Star(i["Proper name"], (i["x"], i["y"])), axis=1)
star_data = star_data.tolist()

con = constellation.Constellation(star_data)
print (con.get_centroid())
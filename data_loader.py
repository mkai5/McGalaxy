import pandas as pd
import star
import constellation

class Data_Loader:

	def import_McDs():
		# Import all McDonalds data
		return pd.read_csv("Mcdonalds_USA_CAN.csv", encoding="latin-1",
			names = ["Longitude","Latitude","City","Information"])

	def import_stars():
		#Import coordinate positions of star data
		star_data = pd.read_csv("hygdata_v3.csv", usecols=["Proper name","x","y","z"])
		#Drop all non-named stars
		star_data = star_data.dropna()
		#Create star instances from star data
		star_data["star instance"]=star_data.apply(
			lambda i: star.Star(i["Proper name"], (i["x"], i["y"])), axis=1)
		return star_data




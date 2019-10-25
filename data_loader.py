import pandas as pd
import constellation
import mcds_con

class Data_Loader:

	def import_McDs():
		# Import all McDonalds data
		mcds_data = pd.read_csv("Mcdonalds_USA_CAN.csv", encoding="latin-1",
			names = ["Longitude","Latitude","City","Information"])
		mcds_data = mcds_data.apply(
			lambda i: mcd.McD(i["City"],(i["Latitude"],i["Longitude"]),
				i["Information"]))
		return mcds_data


	def import_stars():
		#Import coordinate positions of star data
		star_data = pd.read_csv("hygdata_v3.csv", usecols=["Proper name","x","y","z"])
		#Drop all non-named stars
		star_data = star_data.dropna()
		#Create star instances from star data
		star_data=star_data.apply(
			lambda i: star.Star(i["Proper name"], (i["x"], i["y"])), axis=1)
		return star_data




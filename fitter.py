import numpy as np
import pandas as pd
import itertools

import star
import mcd
import constellation
import mcds_con

class Fitter:

	def import_McDs():
		# Import all McDonalds data
		mcds_data = pd.read_csv("Mcdonalds_USA_CAN.csv", encoding="latin-1",
			names = ["Longitude","Latitude","City","Information"])
		mcds_data = mcds_data.apply(
			lambda i: mcd.McD(i["City"],(i["Latitude"],i["Longitude"]),
				i["Information"]), axis=1)
		return mcds_data


	def import_stars():
		#Import coordinate positions of star data
		star_data = pd.read_csv("hygdata_v3.csv", usecols=["Proper name","x","y"])
		#Drop all non-named stars
		star_data = star_data.dropna(subset=["Proper name"])
		#Create star instances from star data
		star_data["Obj"]=star_data.apply(
			lambda i: star.Star(i["Proper name"], (i["x"], i["y"])), axis=1)
		return star_data
	
	def try_fit(con, mcds):
		#calculate constellation centroid
		con_cen = con.get_centroid()
		#print(con_cen)
		con_dist_cen = []
		for i in con.stars:
			con_dist_cen.append(i.dist(i.coordinates,con_cen))
		con_dist_cen.sort()
		for i in range(con.size):
			con_dist_cen[i] = con_dist_cen[i]/con_dist_cen[con.size-1]

		#construct list of things to try
		to_try = list(itertools.combinations(mcds.mcds, con.size))
		#print (to_try)
		best_fit = to_try[0]
		best_total = 100
		print ("Len to_try")
		print (len(to_try))
		for i in to_try:
			mcds_con_i = mcds_con.McDs_con(i)
			mcds_cen = mcds_con_i.get_centroid_mcds()
			temp_list = []
			for j in mcds_con_i.mcds:
				temp_list.append(j.dist(j.coordinates, mcds_cen))
			temp_list.sort()
			for j in range(con.size):
				temp_list[j] = temp_list[j]/temp_list[con.size-1]
			total = 0
			for j in range (con.size):
				total = total + (abs(con_dist_cen[j]-temp_list[j]))
			if (total < best_total):
				best_total = total
				best_fit = mcds_con_i
			#print (i)
		return best_fit


	star_data = import_stars()
	con_data= star_data.loc[(star_data["Proper name"] == "Alioth")
		| (star_data["Proper name"] == "Dubhe")
		| (star_data["Proper name"] == "Merak")
		| (star_data["Proper name"] == "Alkaid")
		| (star_data["Proper name"] == "Phad")
		| (star_data["Proper name"] == "Megrez")
		| (star_data["Proper name"] == "Mizar")]
	#print (con_data)
	star_list = con_data['Obj'].tolist()
	#print (star_list)
	temp_con = constellation.Constellation(star_list)
	temp_mcds = mcds_con.McDs_con(import_McDs().tolist())
	try_fit(temp_con,temp_mcds).print_info()
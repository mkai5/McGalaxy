import numpy as np
import pandas as pd
import itertools

import star
import mcd
import constellation
import mcds_con

class Fitter:

	#Imports McDs data, returns a dataframe including instances
	def import_McDs():
		# Import all McDonald's data from csv
		mcds_data = pd.read_csv("Mcdonalds_USA_CAN.csv", encoding="latin-1",
			names = ["Longitude","Latitude","City","Information"])
		#Create McD instances from McDonald's
		mcds_data = mcds_data.apply(
			lambda i: mcd.McD(i["City"],(i["Latitude"],i["Longitude"]),
				i["Information"]), axis=1)
		return mcds_data

	#Imports star data, returns a dataframe including instances
	def import_stars():
		#import coordinate positions of star data from csv
		star_data = pd.read_csv("hygdata_v3.csv", usecols=["Proper name","x","y"])
		#drop all non-named stars
		star_data = star_data.dropna(subset=["Proper name"])
		#create star instances from star data
		star_data["Obj"]=star_data.apply(
			lambda i: star.Star(i["Proper name"], (i["x"], i["y"])), axis=1)
		return star_data
	
	#Returns best fitting McDs_con given a constellation and an input set of McDs
	def find_best_fit(con, mcds):
		#calculate constellation centroid
		con_cen = con.get_centroid()
		#initialize list of distances from centroid
		con_dist_cen = []
		#populate list
		for i in con.stars:
			con_dist_cen.append(i.dist(i.coordinates,con_cen))
		#sort list
		con_dist_cen.sort()
		#normalize list
		for i in range(con.size):
			con_dist_cen[i] = con_dist_cen[i]/con_dist_cen[con.size-1]

		#construct list of things to try
		to_try = list(itertools.combinations(mcds.mcds, con.size))

		#set base conditions to replace
		best_fit = to_try[0]
		best_total = 100

		#iterate through each McDs_con
		for i in to_try:
			mcds_con_i = mcds_con.McDs_con(i)
			#get centroid
			mcds_cen = mcds_con_i.get_centroid_mcds()
			#initialize list
			dist_list = []
			#create list of distances from centroid
			for j in mcds_con_i.mcds:
				dist_list.append(j.dist(j.coordinates, mcds_cen))
			#sort list
			dist_list.sort()
			#normalize list
			for j in range(con.size):
				dist_list[j] = dist_list[j]/dist_list[con.size-1]
			#check total value of list
			total = 0
			for j in range (con.size):
				total = total + (abs(con_dist_cen[j]-dist_list[j]))
			#if total is better than best so far, replace
			if (total < best_total):
				best_total = total
				best_fit = mcds_con_i
		#return best fitting McDs_con
		return best_fit
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd

import constellation
import mcds_con
import fitter

class McGalaxy:

	#Input Handler
	def handle_input(str_in):
		#pull list of valid constellations from constellation.py
		con_list = constellation.Constellation.constellations
		#by default, use only Alaska McDonald's
		limited = True
		#check for exit condition
		if ((str_in=="x") or (str_in=="exit")):
			return False
		#check for help condition
		elif ((str_in=="h") or (str_in=="help")):
			#print help message
			with pd.option_context('display.max_rows', None, 'display.max_columns', None):
					print("McGalaxy supports the following stars:")
					print (fitter.Fitter.import_stars()["Proper name"].to_string(index=False))
					print ("Any of these stars can be named by proper name, in any sequence")
					print ("McGalay also supports the following constellations:")
					print (con_list)
					print ("Make sure to only use whitespace to delimit your inputs!")
					print ("""Additionally, since the number of McDonald's locations is so large
as to be prohibitive for searching, McGalaxy automatically searches only within Alaska. To
expand your search to all McDonald's in the US and Canada, add the flag "-all" anywhere
within your input, but be warned! It'll take a long time on powerful hardware!""")
			return True
		#otherwise
		else:
			#split the string
			str_list = str_in.split()
			#access its length and store locally
			str_list_len = len(str_list)
			#import star data
			star_data = fitter.Fitter.import_stars()
			#initialize an empty series to hold input stars
			con_data = pd.Series([])
			#initialize index counter to check for two-word stars
			i=0

			#cycle through inputs
			for s in str_list:
				#unlimit is flag present
				if (s=="-all"):
					limited = False
				#if s in a known constellation, treat automatically use
				#	constellation data
				elif (s in con_list):
					#unlimit if flag present
					if ("-all" in str_list):
						limited=False
					#look up constellation data, construct constellation
					con_data = constellation.Constellation.constellation_lookup(s,star_data)
					star_list = con_data['Obj'].tolist()
					feeder_con = constellation.Constellation(star_list)
					#construct McDonald's list
					if (limited):
						feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist()[:31])
					else:
						feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist())
						#remove "-all" flag to make printing prettier
						str_list.remove("-all")
					#print information
					print("The McDonalds that most resemble {} are:".format(feeder_con.list_names()))
					#find best fit
					fitter.Fitter.find_best_fit(feeder_con,feeder_mcds).print_info()
					print('''Input "x" or "exit" to exit or continue exploring the McGalaxy!''')
					return True
				#otherwise, if star is input
				else:
					#append either the star matching the input string, or the
					#	input string and next input string (so two word stars
					# 	can be input)
					con_data = con_data.append(star_data.loc[
						(star_data["Proper name"] == s)])
					if ((i + 1) < str_list_len):
						con_data = con_data.append(star_data.loc[
							(star_data["Proper name"] == (s + " " 
								+ str_list[i+1]))])
				#increment index
				i=i+1

			#build star list
			star_list = con_data['Obj'].tolist()
			#check list has at least 3 entries
			if (len(star_list)<3):
				print("Please input 3 or more valid stars")
				return True
			#build constellation
			feeder_con = constellation.Constellation(star_list)
			#build McDonald's
			if (limited):
				feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist()[:31])
			else:
				feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist())
				str_list.remove("-all")
			print("The McDonalds that most resemble {} are:".format(feeder_con.list_names()))
			#check for best fit
			fitter.Fitter.find_best_fit(feeder_con,feeder_mcds).print_info()
			print('''Input "x" or "exit" to exit or continue exploring the McGalaxy!''')
			return True

		
#Main Function
	
	cycle_loop = True
	#Welcome message
	print ("""Welcome to McGalaxy! This program allows you to input any 
constellation or set of stars, and outputs the set of McDonalds in the US 
and Canada that most resembles it in relative distance and orientation.""")
	print ("""By default, this program limits your search to only Alaska.
However, use the "-all" flag anywhere in your input to search the whole
data set! Be warned, this is extremely long and intensive, and not
feasible for most devices.""")
	print ('''Input "h" or "help" to see what constellations and stars are availible,
or input a constellation or set of stars by proper name below! Exit with "x" or "exit"''')
	#Cycle until user exits
	while (cycle_loop):
		str_in = input()
		cycle_loop=handle_input(str_in)

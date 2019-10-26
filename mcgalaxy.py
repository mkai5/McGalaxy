import pandas as pd

import constellation
import mcds_con
import fitter

class McGalaxy:

	def handle_input(str_in):
		con_list = constellation.Constellation.constellations
		limited = False
		if (str_in=="x"):
			return False
		elif (str_in=="h"):
			with pd.option_context('display.max_rows', None, 'display.max_columns', None):
				print("McGalaxy supports the following stars:")
				print (fitter.Fitter.import_stars()["Proper name"].to_string(index=False))
				print ("Any of these stars can be named by proper name, in any sequence")
				print ("McGalay also supports the following constellations:")
				print (con_list)
				print ("Make sure to only use whitespace to delimit your inputs!")
				print ("""Additionally, since the number of McDonald's locations is so large
as to be prohibitive for searching, flag your list with -a to limit your search to Alaska!""")
				return True
		
		else:

			str_list = str_in.split()
			star_data = fitter.Fitter.import_stars()
			con_data = pd.Series([])

			for s in str_list:
				if (s=="-a"):
					limited = True
					str_list.remove(s)
				elif (s in con_list):
					if ("-a" in str_list):
						limited=True
					con_data = constellation.Constellation.constellation_lookup(s,star_data)
					star_list = con_data['Obj'].tolist()
					feeder_con = constellation.Constellation(star_list)
					if (limited):
						feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist()[:31])
					else:
						feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist())
					print("The McDonalds that most resemble {} are:".format(s))
					fitter.Fitter.try_fit(feeder_con,feeder_mcds).print_info()
					print('''Input "x" to exit or continue exploring the McGalaxy!''')
					return True
				else:
					con_data = con_data.append(star_data.loc[
						(star_data["Proper name"] == s)])

			star_list = con_data['Obj'].tolist()
			if (len(star_list)<=3):
				print("Please input 3 or more valid stars")
				return True
			feeder_con = constellation.Constellation(star_list)
			if (limited):
				feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist()[:31])
			else:
				feeder_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist())
			print("The McDonalds that most resemble {} are:".format(str_list))
			fitter.Fitter.try_fit(feeder_con,feeder_mcds).print_info()
			print('''Input "x" to exit or continue exploring the McGalaxy!''')
			return True



		

	cycle_loop = True
	print ("""Welcome to McGalaxy! This program allows you to input any 
constellation or set of stars, and outputs the set of McDonalds in North 
America that most resembles it.""")
	print ("""Input "h" to see what constellations and stars are availible,
or input a constellation or set of stars by proper name below! Exit
with "x""")
	while (cycle_loop):
		str_in = input()
		cycle_loop=handle_input(str_in)



	'''star_data = fitter.Fitter.import_stars()
	con_data= star_data.loc[(star_data["Proper name"] == "Alioth")
		| (star_data["Proper name"] == "Dubhe")
		| (star_data["Proper name"] == "Merak")
		| (star_data["Proper name"] == "Alkaid")
		| (star_data["Proper name"] == "Phad")
		| (star_data["Proper name"] == "Megrez")
		| (star_data["Proper name"] == "Mizar")]
	print (con_data)
	star_list = con_data['Obj'].tolist()
	temp_con = constellation.Constellation(star_list)
	temp_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist()[31:41])
	fitter.Fitter.try_fit(temp_con,temp_mcds).print_info()'''
import pandas as pd

import constellation
import mcds_con
import fitter

class McGalaxy:

	def handle_input(str_list):
		return 1


	star_data = fitter.Fitter.import_stars()
	con_data= star_data.loc[(star_data["Proper name"] == "Alioth")
		| (star_data["Proper name"] == "Dubhe")
		| (star_data["Proper name"] == "Merak")
		| (star_data["Proper name"] == "Alkaid")
		| (star_data["Proper name"] == "Phad")
		| (star_data["Proper name"] == "Megrez")
		| (star_data["Proper name"] == "Mizar")]
	star_list = con_data['Obj'].tolist()
	temp_con = constellation.Constellation(star_list)
	temp_mcds = mcds_con.McDs_con(fitter.Fitter.import_McDs().tolist()[31:91])
	fitter.Fitter.try_fit(temp_con,temp_mcds).print_info()
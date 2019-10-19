import data_loader as dl
import star
import constellation

class Fitter:
	
	def try_fit(con, mcds):
		#Check lengths of lists
		if (len(con.size)!=len(mcds)):
			raise ValueError("Constellation and McDonalds of different length")





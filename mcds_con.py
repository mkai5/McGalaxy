import mcd

class McDs_con:

	def __init__(self, mcds):
		self.mcds = mcds
		self.size = len(mcds)

	def get_centroid_mcds(self):
		x=0
		y=0
		for i in self.mcds:
			x = x + i.coordinates[0]
			y = y + i.coordinates[1]
		size=len(self.mcds)
		x = x / size
		y = y / size
		return (x,y)

	def print_info(self):
		for i in self.mcds:
			print(i.name, i.info)
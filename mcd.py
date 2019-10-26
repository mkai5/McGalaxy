import math

class McD:

	def __init__(self, name, coordinates, info):
		self.coordinates = coordinates
		self.name = name
		self.info = info

	def dist(self, p0, p1):
		return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
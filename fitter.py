# Algorithm to fit the constelations to the mcdonalds locations
# Marco Kaisth, Ethan Mertz 2019

import math
import csv
import constellation


def try_points(points):
	#con_centroid=constellation.centroid(constellation)
	points_centroid=constellation.centroid(points)
	return points_centroid

try_points([(2,2),(2,3)])
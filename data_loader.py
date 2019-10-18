import pandas as pd

McDs_data = pd.read_csv("Mcdonalds_USA_CAN.csv", encoding="latin-1",
	names = ["Longitude","Latitude","City","Information"])

star_data = pd.read_csv("hygdata_v3.csv", usecols=["Proper name","x","y","z"])
star_data = star_data.dropna()
print (star_data)
import requests
import json
import pandas as pd
from arcgis.gis import GIS
from arcgis.geocoding import reverse_geocode
from arcgis.geometry import Geometry
import math

pd.options.mode.chained_assignment = None

def FindAdress(row):
	if (math.isnan(row['X Coordinate'])) or (math.isnan(row['Y Coordinate'])):
		return None,None,None
	else: 
		pt = Geometry({
		    "x": row['X Coordinate'],
		    "y": row['Y Coordinate'],
		    "spatialReference": {
		        "wkid": 3435
		    }
		})
		try:
			result = reverse_geocode(pt)
			return pd.Series({
				'Neighborhood': result['address']['Neighborhood'],
				'Zipcode': result['address']['Postal'],
				'Address': result})
		except:
			return pd.Series({
				'Neighborhood': None,
				'Zipcode': None,
				'Address': None})





file = 'crimes.csv'

data = pd.read_csv(file)

testData = data[200011:300000]#lower and upper bound of rows your are converting


gis = GIS("https://univofillinois.maps.arcgis.com/home/index.html", "id", "password")


newcolumns = testData.apply(FindAdress,axis=1)
	
testData['Neighborhood'] = newcolumns['Neighborhood']
testData['Zipcode'] = newcolumns['Zipcode']
testData['Address'] = newcolumns['Address']

print(testData.shape)

testData.to_csv('200011To300000.csv')#add name of outputfile. Nameformat: LowerBoundToUpperbound.csv. For example: 0To99.csv



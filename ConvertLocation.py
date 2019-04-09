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
		pt = Geometry({"x": row['X Coordinate'],"y": row['Y Coordinate'],"spatialReference": {"wkid": 3435}})
		result = reverse_geocode(pt)
		return pd.Series({
			'Neighborhood': result['address']['Neighborhood'],
			'Zipcode': result['address']['Postal'],
			'Address': result})





file = 'crimes.csv'

data = pd.read_csv(file)

testData = data[500000:600000]#lower and upper bound of rows your are converting


gis = GIS("https://univofillinois.maps.arcgis.com/home/index.html", "ryousu2.uillinois", "guiliano93")


newcolumns = testData.apply(FindAdress,axis=1)
	
testData['Neighborhood'] = newcolumns['Neighborhood']
testData['Zipcode'] = newcolumns['Zipcode']
testData['Address'] = newcolumns['Address']

print(testData.shape)

testData.to_csv('500000To600000.csv')#add name of outputfile. Nameformat: LowerBoundToUpperbound.csv. For example: 0To99.csv



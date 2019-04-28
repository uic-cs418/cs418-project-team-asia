import pandas as pd
import numpy as np

CrimeData = pd.read_csv('D:/CS 418/cs418-project-team-asia/CrimeNormalized.csv', keep_default_na=False, usecols=range(1,10))
HousePriceData =  pd.read_csv('D:/CS 418/cs418-project-team-asia/neighborByYearNormalized.csv', keep_default_na=False, usecols=range(1,9))

CrimedData = CrimeData.drop(columns='2011',axis=1, inplace=True)
print(CrimeData)

def FindCorrelation(CrimeData, HousePriceData):
	#print(HousePriceData['Region'])
	#print(CrimeData['Neighborhood'])
	CorrelationArray = []
	count = 0
	for neighbourhood in CrimeData['Neighborhood']:
		#print(neighbourhood)
		if neighbourhood in HousePriceData['Region'].unique():
			count = count +1
			NormalizedCrime = CrimeData.loc[CrimeData['Neighborhood'] == neighbourhood].drop(columns='Neighborhood')
			NormalizedHousePrice = HousePriceData.loc[HousePriceData['Region'] == neighbourhood].drop(columns='Region')

			x = np.asarray(NormalizedCrime)[0]
			y = np.asarray(NormalizedHousePrice)[0]
			y = y.astype(np.float)
			correlation = np.corrcoef(x,y)[0, 1]
			print(neighbourhood,correlation)
			CorrelationArray.append([neighbourhood,correlation])
	df = pd.DataFrame(CorrelationArray, columns = ['Neighborhood', 'Correlation'])

	df.to_csv('Correlation_normalized.csv')

FindCorrelation(CrimeData,HousePriceData)



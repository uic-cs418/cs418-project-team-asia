import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


#neighborhoods = data['Neighborhood'].unique()
#groupedByNeighbourhood = data.groupby('Neighborhood')

def predictForNeighbourhood(neighborhood, groupedByNeighbourhood):
	EachMonthCount = getEachMonthCount(neighborhood,groupedByNeighbourhood)
	x = np.arange(EachMonthCount.shape[0])
	y = EachMonthCount['Count']
	model = linear_model.LinearRegression()
	model.fit(x[:,np.newaxis],y[:,np.newaxis])

	x_test = np.arange(EachMonthCount.shape[1],EachMonthCount.shape[1]+24)
	y_pred = model.predict(x_test[:,np.newaxis])
	return y_pred



def getEachMonthCount(neighborhood,groupedByNeighbourhood):
	MonthCount = []
	neighborhoodData = groupedByNeighbourhood.get_group(neighborhood)
	neighborhoodData['Date'] = pd.to_datetime(neighborhoodData['Date'])

	#for neighborhood in neighborhoodData:

	neighborhoodData['YearMonth'] = neighborhoodData['Date'].map(lambda x: 100*x.year + x.month)

	groupedbyYearMonth = neighborhoodData.groupby('YearMonth')
	YearMonths = neighborhoodData['YearMonth'].unique()

	#groupedByYear = neighborhoodData.groupby('Year')
	for yearmonth in YearMonths:
		count = groupedbyYearMonth.get_group(yearmonth).shape[0]
		MonthCount.append([yearmonth,count])
	df = pd.DataFrame(MonthCount, columns = ['Month','Count'])
	df = df.sort_values(by=['Month'])
	return df


def predictForAllNeighborhood(groupedByNeighbourhood, neighborhoods):
	Count2019 = []
	Count2020 = []
	for neighborhood in sorted(neighborhoods):
		y = predictForNeighbourhood(neighborhood,groupedByNeighbourhood)
		x1 = 0
		for i in range(0,12):
			x1 = x1+y[i]
		x2 = 0
		for i in range(12,24):
			x2 = x2+ y[i]
		Count2019.append(np.asscalar(x1))
		Count2020.append(np.asscalar(x2))
	df = pd.DataFrame(sorted(neighborhoods),columns=['Neighborhood'])
	df['2019'] = Count2019
	df['2020'] = Count2020
	return df

CrimeRatioFile = 'CrimeRatio.csv'
ratioDf = pd.read_csv(CrimeRatioFile)



def FindRatio(predictedCrimeNumberDf,ratioDf,File):
	Ratio2019 = []
	Ratio2020 = []

	Total2019 = predictedCrimeNumberDf['2019'].sum()
	Total2020 = predictedCrimeNumberDf['2020'].sum()
	#for neighborhood in predictedCrimeNumberDf['Neighborhood']:
	Ratio2019 = predictedCrimeNumberDf['2019']/Total2019
	Ratio2020 = predictedCrimeNumberDf['2020']/Total2020
	ratioDf['2019'] = Ratio2019
	ratioDf['2020'] = Ratio2020
	ratioDf.to_csv(File)



#pred = predictForAllNeighborhood(groupedByNeighbourhood,neighborhoods)
#FindRatio(pred,ratioDf)








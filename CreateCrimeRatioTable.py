import pandas as pd

file = 'D:/CS 418/Project/Merged/0To2043066.csv' #location of the data file


def CreateCrimeRatioTable(file):
	data = pd.read_csv(file, keep_default_na=False)
	data = data[data['Neighborhood'] != '']
	neighbourhoods = data['Neighborhood'].unique()
	neighbourhoods = neighbourhoods.astype(str)
	neighbourhoods = sorted(neighbourhoods)

	years = data['Year'].unique()
	years = years.astype(int)
	years = sorted(years)

	groupedByYear = data.groupby('Year')
	d = {'Neighborhood':neighbourhoods}
	df = pd.DataFrame(data=d)

	for year in years:
		ratio = FindCrimeRatio(groupedByYear.get_group(year),neighbourhoods)
		df[year] = ratio

	df.to_csv('ratio.csv')#location where to save
	

def FindCrimeRatio(yearData, neighbourhoods):
	totalCount = yearData.shape[0]
	groupedByNeighbourhood = yearData.groupby('Neighborhood')
	ratio = []
	for neighbourhood in neighbourhoods:
		count = 0
		try:
			count = groupedByNeighbourhood.get_group(neighbourhood).shape[0]
		except:
			pass
		ratio.append(count/totalCount)
	return ratio



CreateCrimeRatioTable(file)
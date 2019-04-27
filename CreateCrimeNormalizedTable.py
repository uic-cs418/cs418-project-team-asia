import pandas as pd

file = 'D:/CS 418/Project/Merged/0To2043066.csv' #location of the data file


def CreateCrimeNormalizedTable(file):
	data = pd.read_csv(file, keep_default_na=False)
	data = data[data['Neighborhood'] != '']
	neighbourhoods = data['Neighborhood'].unique()
	neighbourhoods = neighbourhoods.astype(str)
	neighbourhoods = sorted(neighbourhoods)

	years = data['Year'].unique()
	years = years.astype(int)
	#comment
	years = sorted(years)

	groupedByYear = data.groupby('Year')
	d = {'Neighborhood':neighbourhoods}
	df = pd.DataFrame(data=d)

	for year in years:
		normalized = FindNormalizedCrimeNumber(groupedByYear.get_group(year),neighbourhoods)
		df[year] = normalized

	df.to_csv('normalized.csv')#location where to save
	

def FindNormalizedCrimeNumber(yearData, neighbourhoods):
	totalCount = yearData.shape[0]
	groupedByNeighbourhood = yearData.groupby('Neighborhood')
	maxNumber = yearData.groupby('Neighborhood').size().sort_values(ascending=False)[0]
	minNumber = yearData.groupby('Neighborhood').size().sort_values(ascending=True)[0]

	for neighbourhood in neighbourhoods:
		try:
			groupedByNeighbourhood.get_group(neighbourhood).size()
		except:
			minNumber = 0
			break

	#print(maxNumber)
	normalized = []
	for neighbourhood in neighbourhoods:
		count = 0
		try:
			count = groupedByNeighbourhood.get_group(neighbourhood).shape[0]
		except:
			pass
		normalized.append((count-minNumber)/(maxNumber-minNumber))
	return normalized



CreateCrimeNormalizedTable(file)
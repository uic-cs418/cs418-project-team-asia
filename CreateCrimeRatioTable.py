import pandas as pd

def CreateCrimeRatioTable(data,ratioFile,countFile):
	#data = pd.read_csv(file, keep_default_na=False)
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
	dfCount = pd.DataFrame(data=d)

	for year in years:
		ratio,counts = FindCrimeRatio(groupedByYear.get_group(year),neighbourhoods)
		df[year] = ratio
		dfCount[year] = counts

	df.to_csv(ratioFile)#location where to save
	dfCount.to_csv(countFile)
	

def FindCrimeRatio(yearData, neighbourhoods):
	totalCount = yearData.shape[0]
	groupedByNeighbourhood = yearData.groupby('Neighborhood')
	ratio = []
	counts = []
	for neighbourhood in neighbourhoods:
		count = 0
		try:
			count = groupedByNeighbourhood.get_group(neighbourhood).shape[0]
		except:
			pass
		counts.append(count)
		ratio.append(count/totalCount)
	return ratio,counts

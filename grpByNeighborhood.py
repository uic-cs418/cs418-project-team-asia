import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("0To500010.csv")
groupByNeighborhood = df.groupby('Neighborhood')
selectedNeighborhood = groupByNeighborhood.get_group('Austin')
print(len(groupByNeighborhood))

def plotCrimeNumbers(neighborhood):
	neighborhoodData = groupByNeighborhood.get_group(neighborhood)
	neighborhoodData['Date'] = pd.to_datetime(neighborhoodData['Date'])
	neighborhoodData['Year'] = pd.DatetimeIndex(neighborhoodData['Date']).year
	groupedByYear = neighborhoodData.groupby('Year')
	DataToPlot = pd.DataFrame(data = groupedByYear.size().reset_index(name='Counts'))
	#DataToPlot.columns = ['Year','Count']
	#print(DataToPlot['Count'])
	sns.lineplot(x="Year", y="Counts", data=DataToPlot)
	ax = plt.gca()
	ax.set_xticks(np.arange(DataToPlot['Year'][0], DataToPlot['Year'][DataToPlot['Year'].count()-1]+1 , 1))
	plt.show()

plotCrimeNumbers('Loop')
plotCrimeNumbers('Irving Park')
plotCrimeNumbers('Englewood')
plotCrimeNumbers('Auburn Gresham')

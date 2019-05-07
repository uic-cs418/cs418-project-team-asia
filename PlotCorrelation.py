import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file = 'D:/CS 418/cs418-project-team-asia/Correlation_ratio.csv'

Correlations = pd.read_csv(file, usecols=range(1,5))

def positiveOrNegative(row):
    if row['Correlation'] >= 0:
        val = 'Positive'
    else:
        val = 'Negative'
    return val

def PlotCorrelation(CorrelationsData):
	#CorrelationsData['PositiveOrNegative'] = CorrelationsData.apply(positiveOrNegative,axis=1)
	X = np.arange(CorrelationsData.shape[0])
	sns.scatterplot(x=X,y=CorrelationsData['Correlation'],hue=CorrelationsData['Significance'])
	plt.title('Significance of Correlations Between Crime Ratio and House Price Ratio of Each Neighborhood(2012-2018)')
	plt.xlabel('Observation Number(Neighborhoods)')
	plt.show()

PlotCorrelation(Correlations)
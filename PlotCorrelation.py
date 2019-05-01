import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file = 'D:/CS 418/cs418-project-team-asia/Correlation_ratio.csv'

Correlations = pd.read_csv(file, usecols=range(1,3))

def positiveOrNegative(row):
    if row['Correlation'] >= 0:
        val = 'Positive'
    else:
        val = 'Negative'
    return val

def PlotCorrelation(CorrelationsData):
	CorrelationsData['PositiveOrNegative'] = CorrelationsData.apply(positiveOrNegative,axis=1)
	X = np.arange(CorrelationsData.shape[0])
	sns.scatterplot(x=X,y=CorrelationsData['Correlation'],hue=CorrelationsData['PositiveOrNegative'])
	plt.show()

PlotCorrelation(Correlations)
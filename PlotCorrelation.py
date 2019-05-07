import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def positiveOrNegative(row):
    if row['Correlation'] >= 0:
        val = 'Positive'
    else:
        val = 'Negative'
    return val

def PlotCorrelation(CorrelationsData,hue,title):
	CorrelationsData['PositiveOrNegative'] = CorrelationsData.apply(positiveOrNegative,axis=1)
	X = np.arange(CorrelationsData.shape[0])
	sns.scatterplot(x=X,y=CorrelationsData['Correlation'],hue=CorrelationsData[hue])
	plt.title(title)
	plt.xlabel('Observation Number(Neighborhoods)')
	plt.show()
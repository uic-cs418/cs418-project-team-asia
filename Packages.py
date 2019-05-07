import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from CreateCrimeRatioTable import CreateCrimeRatioTable
from functions1 import removingJunk,makingAggTable,makeRatio,plotTogether,housePred
from FindCorrelation import FindCorrelation
from PlotCorrelation import PlotCorrelation
from LinearRegressionCrime import predictForAllNeighborhood, FindRatio
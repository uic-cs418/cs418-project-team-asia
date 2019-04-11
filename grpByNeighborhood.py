import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("0To9999.csv")
groupByNeighborhood = df.groupby('Neighborhood')
selectedNeighborhood = groupByNeighborhood.get_group('Austin')
print(selectedNeighborhood.head(2))

#for name, grp in groupByNeighborhood:
    #print(name)
    #print(grp)

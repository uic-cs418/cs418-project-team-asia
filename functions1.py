#given dataframe, neighborhood name, year, return the avg ppsf for that year for that neighborhood
def fun(df, neighborhood, year):
    cnt = 0.0
    total = 0

    for e,f,g in zip(df['Region'],df['Period Begin'],df['Median Ppsf']):
        date = f.split("/")
        try:
            if int(date[2]) == year and e == neighborhood:
                cnt = cnt + 1
                total = total + float(g)
        except:
            pass

    return total/cnt


#just a plotting, don't need in the final report
def plot(df, neighborhood):
    x = np.zeros(7)
    
    y=[2012,2013,2014,2015,2016,2017,2018]
    
    for i in y:
        x[i-2012]=fun(df, neighborhood,i)
    
    fig = plt.figure()
    plt.plot(y, x)
    fig.suptitle('Housr price in ppsf for '+neighborhood+' by each year')
    plt.xlabel('year')
    plt.ylabel('price per square feet')





#making aggregated table for house price and returning that table
def makingAggTable(df1):
    neighborhoods=df1.Region.unique()

    fulldf=pd.DataFrame()

    for neigh in neighborhoods:
        x = np.zeros(7)
        y=[2012,2013,2014,2015,2016,2017,2018]
        for i in y:
            x[i-2012]=fun(df1,neigh,i)
            
        data={'Region':[neigh],'2012':[x[0]],'2013':[x[1]],'2014':[x[2]],'2015':[x[3]],'2016':[x[4]],'2017':[x[5]],'2018':[x[6]]}
        singlerow=pd.DataFrame(data)
        fulldf=fulldf.append(singlerow, ignore_index=True)

    return fulldf


def removingJunk(df1):
    
    for i in range(len(df1)):
        name=df1.iloc[i, 0]
        df1.iloc[i, 0]=name.replace("Chicago, IL - ","")
        
    return df1




#making ratio df from aggregated df, input numofYear as 7 for 2012-2018, 9 for 2012-2020
def makeRatio(fulldf, numofYear):

    countdf=fulldf.copy()
    
    for i in range(numofYear):
        maxvalue=countdf.iloc[:,i+1].max()
        minvalue=countdf.iloc[:,i+1].min()
        sumvalue=countdf.iloc[:,i+1].sum()
        rangevalue=maxvalue-minvalue
        for j in range(len(countdf)):
            countdf.iloc[j, i+1]=countdf.iloc[j, i+1]/sumvalue

    return countdf


#house is house price ratio df, crime is crime ratio df, neigh is name of the neighborhood
def plotTogether(neigh, crime, house):
    singlerowhouse=house[house['Region']==neigh]
    singlerowcrime=crime[crime['Neighborhood']==neigh]
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot([2012,2013,2014,2015,2016,2017,2018], singlerowhouse.iloc[0,1:8], 'b-')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    

    ax2 = ax1.twinx()
    ax2.plot([2012,2013,2014,2015,2016,2017,2018], singlerowcrime.iloc[0,1:8], 'r-')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
    
    ax1.set_title('House price ratio and Crime ratio for '+neigh)
    ax1.set_xlabel('time (year)')
    ax1.set_ylabel('House Price Ratio')
    ax2.set_ylabel('Crime Ratio')
    
    fig.savefig(neigh+'.png',bbox_inches='tight')



#df1 is house price df before aggregation, count is df after aggregation
def housePred(df1, count):
    newdf=df1.copy()
    newcount=count.copy()
    
    newdf=newdf[newdf['Median Ppsf']!='']
    groupbydata=newdf.groupby('Region')
    
    sumlist1=[]
    sumlist2=[]
    for i in range(len(count)):
        name=newcount.iloc[i,0]
        
        selectedone = groupbydata.get_group(name)
        x = np.arange(len(selectedone))
        y = selectedone['Median Ppsf']
        
        #print(name,y)
        
        regr = linear_model.LinearRegression()
        # Train the model using the training sets
        regr.fit(x[:,np.newaxis], y[:,np.newaxis])
        x_test = np.arange(87,115)
        # Make predictions using the testing set
        y_pred = regr.predict(x_test[:,np.newaxis])
        
        sumvalue1=0
        sumvalue2=0
        for j in range(12):
            sumvalue1=sumvalue1+y_pred[j]
            sumvalue2=sumvalue2+y_pred[j+12]
            
        sumlist1.extend(sumvalue1/12)
        sumlist2.extend(sumvalue2/12)
        
    
    newcount['2019']=sumlist1
    newcount['2020']=sumlist2
        
    return newcount


print('done')


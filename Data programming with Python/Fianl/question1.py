# -*- coding: utf-8 -*-
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series

w1 = pd.read_csv('weather1.csv')
pc=stats.pearsonr(w1.min_temp, w1.max_temp)
#Ans:0.8280922601815279

w2=pd.read_csv('weather2.csv')
w12=pd.merge(w1,w2,on=['date','station'])

plt.figure()
plt.scatter(w12.mean_temp,w12.mean_wind)
plt.show()

w3=pd.read_csv('weather3.csv')
w123=pd.concat([w12,w3],sort=False)
w123.iloc[w123.min_temp.idxmin()]
#Ans:Dec-10,DublinAirport,-12.2


w123['Month']=0
w123['Year']=0
j=0
for i in w123.date:
    w123['Month'].iloc[j]=i.split('-')[0]
    w123['Year'].iloc[j]=i.split('-')[1]
    j=j+1


w123 = w123.drop('date',axis=1)
month=w123.Month
year=w123.Year
w123 = w123.drop('Month',axis=1)
w123 = w123.drop('Year',axis=1)

w123.insert(0,'Year',year)
w123.insert(0,'Month',month)







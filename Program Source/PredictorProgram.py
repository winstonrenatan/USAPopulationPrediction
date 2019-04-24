from sklearn import metrics
from scipy import stats
import pandas as pd
import numpy as np 
import math

df = pd.read_csv('USAPopulationStart.csv')

# Calculate Mean
MeanX=2013.0    #Final and never changes
df['meanY']=(df.iloc[:, 10:17].sum(axis=1))/7

# Deviation of X never changes. (SS_XX = np.sum(x*x) - n*m_x*m_x)
SS_XX=28.0
# Cross Deviation of X and Y (Subtract Yi with Mean then multiple with Xi subtracted with mean)
# Subtract Xi with mean: is absolute Year and its mean never change (2013.0)
df['SS_XY']=((df['2010']-df['meanY'])*-3)+((df['2011']-df['meanY'])*-2)+((df['2012']-df['meanY'])*-1)+((df['2013']-df['meanY'])*0)+((df['2014']-df['meanY'])*1)+((df['2015']-df['meanY'])*2)+((df['2016']-df['meanY'])*3)

# Regression Coefficients
df['b_1']=df['SS_XY']/SS_XX
df['b_0']=df['meanY']-df['b_1']*MeanX

# Prediction for Year
df['2013PRED']=df['b_0']+df['b_1']*2013 #Is used to count the error rate
df['2017PRED']=df['b_0']+df['b_1']*2017
df['2018PRED']=df['b_0']+df['b_1']*2018
df['2019PRED']=df['b_0']+df['b_1']*2019
df['2020PRED']=df['b_0']+df['b_1']*2020

# Save file to a csv formated file
df.to_csv('USAPopDeci.csv')
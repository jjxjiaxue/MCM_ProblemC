#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error,mean_squared_error,median_absolute_error,r2_score
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
#读取工作簿和工作簿中的工作表
data_frame=pd.read_excel('Problem_C_Data_Wordle.xlsx')

data = list(reversed(data_frame.loc[ 1: ,"Unnamed: 4"].tolist()))
data=data[28:]
length=len(data)
ydata = data
xdata = [ i for i in range(length)]

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
 
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

plt.plot(xdata,ydata,'b-')
popt, pcov = curve_fit(func, xdata, ydata)
#popt数组中，三个值分别是待求参数a,b,c
y2 = [func(i, popt[0],popt[1],popt[2]) for i in xdata]
plt.plot(xdata,y2,'r--')
print(popt)


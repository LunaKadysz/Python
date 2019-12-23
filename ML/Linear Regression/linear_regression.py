# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:04:08 2019

@author: Luna Kadysz
"""

import numpy as np
import statsmodels.api as sm

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

x = sm.add_constant(x) #add the column of ones to the inputs if you want statsmodels to calculate the intercept. It doesn’t takes it into account by default


model = sm.OLS(y, x)
results = model.fit()

#print(results.summary())
print('coefficient of determination:', results.rsquared)
print('adjusted coefficient of determination:', results.rsquared_adj)
print('regression coefficients:', results.params)

print('predicted response:', results.fittedvalues, sep='\n')
print('predicted response:', results.predict(x), sep='\n')

x_new = sm.add_constant(np.arange(10).reshape((-1, 2)))
y_new = results.predict(x_new)


#hardcoded just to check

def f(x1,x2,m,n,b):
    return m*x1 +n*x2 + b

m = 0.4471
n = 0.2550
b = 5.5226
resp = f(x[:,1],x[:,2],m,n,b)
print('resultadoss:', resp, sep='\n')



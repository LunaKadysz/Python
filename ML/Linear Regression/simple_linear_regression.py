# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:51:35 2019

@author: Luna Kadysz
"""

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y) ## compact: model = LinearRegression().fit(x, y)

r_sq = model.score(x, y) ## R**2
print('coefficient of determination:', r_sq)
print('b:', model.intercept_)
print('slope:', model.coef_)


y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')


#hardcoded just to check

def f(x,m,b):
    return m*x + b

resp = f(np.arange(10).reshape((-1, 2)),model.coef_,model.intercept_)
print(resp)
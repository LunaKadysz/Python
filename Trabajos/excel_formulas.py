# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:50:27 2019

@author: Luna Kadysz
"""

import formulas
import pandas as pd
import numpy as np


fpath = 'EXTRA_BALCON.XLSX'
xl_model = formulas.ExcelModel().loads(fpath).finish()
print(xl_model.calculate())







#def csvDf(dat,**kwargs): 
#  from numpy import array
#  data = array(dat)
#  if data is None or len(data)==0 or len(data[0])==0:
#    return None
#  else:
#    return pd.DataFrame(data[1:,1:],index=data[1:,0],columns=data[0,1:],**kwargs)
#
#csvDf(np.reshape(tabla,(61,36))).to_html('test.html') # Export the DataFrame (Excel doc) to an html file 
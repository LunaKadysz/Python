# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:11:31 2019

@author: Luna Kadysz
"""
import pandas as pd
import numpy as np
#import urllib.request
#urllib.request.urlopen('http://www.ewbi.com/ewbi.develop/samples/jsport_nonEAT.html')
#tabla = pd.read_excel('EXTRA_BALCON.XLSX')
from openpyxl import load_workbook

wb = load_workbook(filename = 'EXTRA_BALCON.XLSX')
sheet_names = wb.get_sheet_names()
name = sheet_names[0]
sheet_ranges = wb[name]
tabla = pd.DataFrame(sheet_ranges.values)
tabla = np.array(tabla)
tabla = tabla[1:62,4:]
np.reshape(tabla,(1,2196))
=










def csvDf(dat,**kwargs): 
  from numpy import array
  data = array(dat)
  if data is None or len(data)==0 or len(data[0])==0:
    return None
  else:
    return pd.DataFrame(data[1:,1:],index=data[1:,0],columns=data[0,1:],**kwargs)

csvDf(np.reshape(tabla,(61,36))).to_html('test.html') # Export the DataFrame (Excel doc) to an html file 
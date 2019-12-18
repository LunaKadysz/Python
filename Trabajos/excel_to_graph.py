# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:41:53 2019

@author: Luna Kadysz
"""
import pandas as pd
import numpy as np
from pycel import ExcelCompiler
from IPython.display import FileLink
import matplotlib.pyplot as plt


filename = "EXTRA_BALCON.XLSX"
print("Loading {}...".format(filename))

# load & compile the file to a graph
excel = ExcelCompiler(filename=filename)

print(excel.__dict__)

print("Plotting using matplotlib...")
#excel.plot_graph()
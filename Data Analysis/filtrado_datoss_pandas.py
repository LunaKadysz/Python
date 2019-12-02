# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:03:41 2019

@author: Luna Kadysz
"""


import pandas as pd
from pandas import DataFrame
import numpy as np

nombres = ['system.owned_by','Documentacion.cuil','Solicitud_Credito.Nombre','Solicitud_Credito.Banco','Solicitud_Credito.CBU','Solicitud_Credito.Nro_de_Comercializadora','Solicitud_Credito.empleadorDelSocio','Reporte_Nosis.Empleador','Reporte_Nosis.Domicilio','Datos_de_la_DB_de_CS.listaNegra']
nombres_db = ['SystemOwner','Cuil','Name','BankName','CBU','Nro_Comercializadora','Employer','NosisEmployer','Adress','BlackList']
numero = [64,339,375,369,370,87,273,69,73,174]
file = pd.read_excel("nbch.xlsx")
data=[]

for n in numero:
   columna = file.iloc[:,n]
   columna.pop(0)
   data.append(columna)


def dataFiltrada(data):
    datos = np.array(data)
    d = datos.transpose()
    print(np.shape(d))
    for i in reversed(range(len(d)-1)):
        if str(d[i,1]) == 'nan':
            d = np.delete(d, i, 0)
    return d.transpose()
            

SystemOwnerDictionary = dict(zip(nombres_db[0], list(dataFiltrada(data)[0])))
ComercializadoraCredisimpleDictionary = dict(zip(nombres_db[5], list(dataFiltrada(data)[5])))
ClientDictionary = dict(zip(nombres_db[0:3] + nombres_db[4:9],list(dataFiltrada(data)[0:3]) +list(dataFiltrada(data)[4:9])))
AdressDictionary = dict(zip(nombres_db[8], list(dataFiltrada(data)[8])))
BankDictionary = dict(zip(nombres_db[3:5], list(dataFiltrada(data)[3:5])))
EmployerDictionary = dict(zip(nombres_db[6:8], list(dataFiltrada(data)[6:8])))




dfSystemOwner = DataFrame([SystemOwnerDictionary])
dfComercializadoraCredisimple = DataFrame([ComercializadoraCredisimpleDictionary])
dfClient = DataFrame([ClientDictionary])
dfAdress = DataFrame([AdressDictionary])
dfBank = DataFrame([BankDictionary])
dfEmployer = DataFrame([EmployerDictionary])


export_csv1 = dfSystemOwner.to_csv ('nbchSystemOwner.csv', index = None) 
export_csv2 = dfComercializadoraCredisimple.to_csv ('nbchComercializadoraCredisimple.csv', index = None) 
export_csv3 = dfClient.to_csv ('nbchClient.csv', index = None) 
export_csv4 = dfAdress.to_csv ('nbchAdress.csv', index = None) 
export_csv5 = dfBank.to_csv ('nbchBank.csv', index = None) 
export_csv6 = dfEmployer.to_csv ('nbchEmployer.csv', index = None) 



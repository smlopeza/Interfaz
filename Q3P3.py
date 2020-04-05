#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import datetime as dt
import Script_entradas as SE
from copy import deepcopy

""" Este incluye lluvia entonces es trihorario"""

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

"""
def CargarPMC(ruta):
	# Carga los metadatos internos del archivo .json
	archivo_disco=open(ruta+'.json','r')
	archivo_ram=archivo_disco.read()
	archivo_disco.close()
	rn=model_from_json(archivo_ram)

	# Carga los pesos de la red neuronal del archivo .h5
	rn.load_weights(ruta+'.h5')

	return rn #devuelve la red
"""

def Modelo3_(Caudales_Amoya,PPT):

	print (Caudales_Amoya)
	#PPT = SE.Read_WRF_Amoya(ruta_ppt)
	#Caudales_Amoya = SE.Lectura_Q(ruta_q)

	#Hora_format = dt.datetime.now()

	Hora_format = dt.datetime.strptime('2019-06-07 07:00:00','%Y-%m-%d %H:%M:%S')
	hrs_disp = np.arange(1,24,3)
	nearest_hour = find_nearest(hrs_disp,Hora_format.hour)
	date_loc = dt.datetime.strptime(str(Hora_format.date())+' '+ "%02d" % nearest_hour+':00:00','%Y-%m-%d %H:%M:%S')

	entradas=np.zeros((1,5))

	Values_Q = []
	for i in [9,6,3]:
		Values_Q.append(Caudales_Amoya.loc[date_loc-dt.timedelta(hours=i)].values[0])

	Fechas_pronostico = PPT[date_loc:].index
	"""
	for Date in Fechas_pronostico:

		print (Date)
		entradas[:,0] = Values_Q[-3]
		entradas[:,1] = Values_Q[-2]
		entradas[:,2] = Values_Q[-1]
		entradas[:,3] = PPT.loc[Date-dt.timedelta(hours=6)].values
		entradas[:,4] = PPT.loc[Date-dt.timedelta(hours=3)].values

		rn = CargarPMC('/mnt/c/Users/Silvana M/Documents/Contratos/Gotta_Amoya/00_FINAL/01_SCRIPTS/Redes/PorHorizonte/Q3P3/model')
		val_pron=rn.predict(entradas)[:,0]
		Values_Q = np.append(Values_Q, val_pron)

	Pronostico = pd.DataFrame({'Caudal_pronosticado':Values_Q[-len(Fechas_pronostico):]},index= Fechas_pronostico)
	#if ruta_save != None:
	#	Pronostico.to_csv(ruta_save+'.csv')
	"""
	return Fechas_pronostico


"""
ruta_save = ''#donde quieran guardar esa monda y ahi mismo le pueden poner el fackin nombre
ruta_redes ='/mnt/c/Users/Silvana M/Documents/Contratos/Gotta_Amoya/00_FINAL/01_SCRIPTS/Redes/PorHorizonte/'# Aca es la ruta donde yo tengo guardada la red neuronal. Todo va en el correo. Fuck deberia subir esto a git

#Ejemplo lectura  PPT
ruta_ppt = '/mnt/c/Users/Silvana M/Documents/Contratos/Gotta_Amoya/00_FINAL/00_ENTRADAS/DatosEntrada/Lluvia/Raw_data/72horas/2019060112/'

#Ejemplo lectura Q
ruta_q = '/mnt/c/Users/Silvana M/Documents/Contratos/Gotta_Amoya/00_FINAL/00_ENTRADAS/DatosEntrada/Caudal/csv/Caudal_Amoya.csv'

PPT = SE.Read_WRF_Amoya(ruta_ppt)
print (PPT)

Caudales_Amoya = SE.Lectura_Q(ruta_q)

print (Caudales_Amoya)




Pronostico = Modelo3_(Caudales_Amoya,PPT)
"""
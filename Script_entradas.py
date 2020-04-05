#!/usr/bin/env python
#-*- coding:utf-8 -*-


import numpy as np 
import glob
import pandas as pd
import datetime as dt


#########################################################################################################
# Entradas Lluvia modelo WRF                                                                            
#########################################################################################################
def Read_WRF_Amoya(ruta_global,ruta_save=None):

	lats =  np.loadtxt(open(ruta_global+'Amoya_lat.csv', "rb"))
	lons =  np.loadtxt(open(ruta_global+'Amoya_lon.csv', "rb"))

	#Mascara
	ZonaAlta2 = np.zeros((5,5))*np.nan
	ZonaAlta2[0,0:2]= 1
	mask= ZonaAlta2

	#Lectura
	fechas = []
	values = []
	serie_promedio= []
	#for F in Folders:
	data = glob.glob(ruta_global+'Amoya_ppt05*.csv')
	data.sort()
	if len(data)!=0:
	    for D in data:
	        #print (D)
	        vals = np.loadtxt(open(D, "rb"))
	        fechas.append(D[-14:-4])
	        values.append(vals*mask)
	        serie_promedio.append(np.nansum(vals*mask))

	#Reindexeo, organizacion fechas en datetime
	fechas_dt = [dt.datetime.strptime(date_string, '%Y%m%d%H') for date_string in fechas]
	mean_df = pd.DataFrame({'PromedioAcum3h_ZonaAlta2':serie_promedio},index=fechas_dt)
	reindex =  pd.date_range(fechas_dt[0],periods=25,freq='3H')
	mean_df_r = mean_df.reindex(reindex,fill_value=np.nan)
	if ruta_save != None:
		Date_init = fechas_dt[0]
		save_date = str(Date_init.year) + str("%02d" % Date_init.month) + str("%02d" % Date_init.day)
		mean_df_r.to_csv(ruta_save+'Precipitacion_WRF_ZonaAlta2_'+save_date+'.csv')
	return mean_df_r


#########################################################################################################
# Entradas Caudal                                                                            
#########################################################################################################

def Lectura_Q(ruta_q):
	"""
	Q = pd.read_csv(ruta_q)#los datos estan completos
	Q['Unnamed: 0'] = [dt.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S') for temp in Q['Unnamed: 0'].values ]
	Q.set_index('Unnamed: 0',inplace=True)
	"""

	Q = pd.read_csv(ruta_q)#los datos estan completos
	Q['Unnamed: 0'] = [dt.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S') for temp in Q['Unnamed: 0'].values ]
	Q = Q.set_index('Unnamed: 0')
	return Q


def Analiza_Calidad(Data,N1 = 4.0, N2 = 2.0, N3 = 0.2):
    """
    ### Filtros
     Codigo para analizar la calidad de las series de caudales de ISAGEN
     
     La idea es tener 4 categorías:
     
     *  0 para los datos buenos.
     *  1 para los datos outlier, los que son demasiado evidentes
     *  2 para los datos dudosos, mediante x-IQR o x-desviaciones estándar
     *  3 para los datos faltantes.
    """
    
    # Obtiene la informacion cruda
    DataMask = np.ma.array(Data,mask=np.isnan(Data))
    #Genera el vector de calidad 
    Calidad = np.zeros(Data.shape)
    #Flag por dato ausente 
    Calidad[np.isnan(Data)] = 3
    #Flag por dato atipico Considerado como X > N*Desv o X > N*Q99
    P90 = np.percentile(Data[np.isfinite(Data)],90)
    P50 = np.percentile(Data[np.isfinite(Data)],50)
    #Flag para dato dudoso 
    Calidad[DataMask > P90 * N2] = 2
    Calidad[DataMask < P50 * N3] = 2
    Calidad[DataMask > P90 * N1] = 1

    return Calidad 


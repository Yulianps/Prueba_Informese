import re
import pandas as pd
import numpy as np
from functools import reduce


def process_ejercicio3 ():
    
    #Creamos las 3 columnas de valores de texto
    lst = 25*['a', 'b', 'c', 'd']
    dfrand_t = pd.DataFrame(list(zip(lst, lst,lst)),columns=list('123'))

    #Creamos las 7 columnas faltantes pobladas con enteros del 1 al 100

    dfrand_n1 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))
    dfrand_n2 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))

    #Creamos los  dataframes resultantes con las condiciones requeridas

    dfrand_1 = pd.concat([dfrand_t,dfrand_n1], axis=1)
    dfrand_2 = pd.concat([dfrand_t,dfrand_n2], axis=1)

    print("Para DF's diferentes -->")
    comparacion = comparar(dfrand_1, dfrand_2)

    print("Para DF's iguales -->")
    comparacion = comparar(dfrand_1, dfrand_1)

    return

#Función comparar retorna el porcentaje de registros iguales que hay en dos dataframes comparandolos

def comparar (df1, df2):    
    result = (df1 == df2)
    
    conteo = result[result == True].count()
    sumatoria = reduce(lambda a,b : a+b, conteo)
    porcentaje = sumatoria/(result.shape[0]*result.shape[1])*100
    print("El porcentaje de registros iguales en los dos dataframes es de: ")
    print(str(porcentaje) + " %")
    return 
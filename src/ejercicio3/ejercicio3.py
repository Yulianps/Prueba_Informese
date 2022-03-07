import re
import pandas as pd
import numpy as np

def process_ejercicio3 ():
    #Creamos las 3 columnas de valores de texto
    # ind= range(99)
    lst = 25*['a', 'b', 'c', 'd']
    dfrand_t = pd.DataFrame(list(zip(lst, lst,lst)),columns=list('123'))

    #Creamos el resto de columnas

    dfrand_n1 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))
    dfrand_n2 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))

    #Creamos el dataframe resultante

    dfrand_1 = pd.concat([dfrand_t,dfrand_n1], axis=1)
    dfrand_2 = pd.concat([dfrand_t,dfrand_n2], axis=1)

    # print(dfrand_2.head(210))
    print("Para DF's diferentes -->")
    comparacion = comparar(dfrand_1, dfrand_2)

    print("Para DF's iguales -->")
    comparacion = comparar(dfrand_1, dfrand_1)
    # freq = comparacion.groupby(['1', '6']).size() 
    # print(comparacion)

    #print(df_rand_2.head(200))
    return


def comparar (df1, df2):    
    result = (df1 == df2)
    # print(result.shape)
    conteo = result[result == True].count()
    # print(conteo)
    
    suma = 0
    for i in range(0,result.shape[1]):
        suma = suma + conteo[i]
    
    # print(suma)
    porcentaje = suma/(result.shape[0]*result.shape[1])*100
    print("El porcentaje de registros iguales en los dos dataframes es de: ")
    print(str(porcentaje) + " %")
    return conteo
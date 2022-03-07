import re
import pandas as pd
import numpy as np



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
    print(porcentaje)
    return conteo

#Creamos las 3 columnas de valores de texto
# ind= range(99)
lst = 25*['a', 'b', 'c', 'd']
dfrand_t = pd.DataFrame(list(zip(lst, lst,lst)),columns=list('123'))

#Creamos el resto de columnas

dfrand_n1 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))
dfrand_n2 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))

#Creamos los dataframes resultantes

dfrand_1 = pd.concat([dfrand_t,dfrand_n1], axis=1)
dfrand_2 = pd.concat([dfrand_t,dfrand_n2], axis=1)

# print(dfrand_2.head(210))

# comparacion = comparar(dfrand_1, dfrand_2)
# print(comparacion)

comparacion = comparar(dfrand_1, dfrand_2)
# freq = comparacion.groupby(['1', '6']).size() 
print(comparacion)

#print(df_rand_2.head(200))
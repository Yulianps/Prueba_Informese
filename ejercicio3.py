import pandas as pd
import numpy as np

#Creamos las 3 columnas de valores de texto
ind= range(99)
lst = 25*['a', 'b', 'c', 'd']
dfrand_t = pd.DataFrame(list(zip(lst, lst,lst)),columns=list('123'))

#Creamos el resto de columnas

dfrand_n1 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))
dfrand_n2 = pd.DataFrame(np.random.randint(0,100,size=(100, 7)), columns=list('4567890'))

#Creamos el dataframe resultante

dfrand_1 = pd.concat([dfrand_t,dfrand_n1], axis=1)
dfrand_2 = pd.concat([dfrand_t,dfrand_n2], axis=1)

 
result = (dfrand_1 == dfrand_2)
freq = result.groupby(np.column_stack).size()



#print(df_rand_2.head(200))
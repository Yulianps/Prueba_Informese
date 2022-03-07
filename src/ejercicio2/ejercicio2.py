import pandas as pd
import matplotlib.pyplot as plt
import json

def process_ejercicio2(input_path: str):
    
    #Leemos el archivo de texto ejercicio2_b1 en el path donde se haya descargado 
    with open(input_path,'r') as f: 
        data = json.loads(f.read())
    dfjson = pd.json_normalize(data, record_path =['ventas'])

    #print(dfjson.describe())

    #Haciendo una inspección de las estadísticas del DF original vemos que graficarlas no permitirá una buena visualización

    #Se procede a separar la columna tiempo en año y Cuartos para una mejor visualización de las estadísticas

    quaters = dfjson["tiempo"].str.split('-', expand=True)
    quaters.columns = ['Año', 'Cuartos']
    print(dfjson)

    dfjson = pd.concat([quaters, dfjson], axis=1)
    print(dfjson)

    #Se agrupa por el campo Cuarto para visualizar el comportamiento del total de las ventas en cada cuarto

    # dfjson = dfjson.groupby(['Cuarto'])['ValorVenta'].describe()

    #Las estadísticas agrupadas no nos dan una idea clara para graficarlas puesto que se mezclan valores con porcentajes etc..

    #Por eso se procede a graficar por separado los datos de las estadísticas que sí generen un gráfica útil para analizar

    dfjson_quaters = dfjson.groupby(['Cuartos'])['ValorVenta'].sum()
    print(dfjson_quaters)

    plot_sum = dfjson_quaters.plot.bar()

    plt.show()


    # dfjson_total = dfjson.groupby(['Cuarto'])['ValorVenta'].count()

    # print(dfjson_total)
    
    return


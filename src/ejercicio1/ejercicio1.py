# Importamos las librerías necesarias
import pandas as pd
import csv

def process_ejercicio1 (input_path1: str, input_path2: str, output_path: str):
    
    #Leemos la BD Excel ejercicio1 en el path donde se haya descargado dentro de la carpeta inputs 
    #Al hacer inspección inicial de la BD encontramos que la columna E contiene datos indeseados y no se carga en el DF
    
    exceldf = pd.read_excel(input_path1, usecols = 'A:D')
    
    # Se eliminan registros nulos y duplicados de la columna id
    
    exceldf = exceldf.dropna(subset=["id"])
    exceldf = exceldf.drop_duplicates(exceldf.columns[~exceldf.columns.isin(['id'])])

    # Normalizamos la columna Tipo de pedido
    exceldf['Tipo de pedido'] = exceldf['Tipo de pedido'].str.upper()
    exceldf['Tipo de pedido'] = exceldf['Tipo de pedido'].str.replace(" ","")
    exceldf['Tipo de pedido'] = exceldf['Tipo de pedido'].str.replace("SIN_INFO","SININFO")

    #Renombramos la columna cc_cliente     
    exceldf.rename(columns={'cc_cliente': 'CEDULA'}, inplace=True)

    # 
    grouped_excel_data = exceldf.groupby(['CEDULA', 'Tipo de pedido'], as_index=False)['numero de pedido' ].count()
    grouped_excel_data.rename(columns={'numero de pedido': 'Cantidad número de pedido'}, inplace=True)

    #Imprimimos la salida pedida en el iteral C de la prueba
    print (grouped_excel_data)

    #Leemos archico texto plano ejercicio1_b2.txt 
    textdf = pd.read_table(input_path2, header= 0)

    #Creamos la columna NOMBRE COMPLETO con la primera letra de apellido y nombre en mayúsculas
    textdf['NOMBRE COMPLETO'] = textdf['NOMBRE'].str.capitalize() + " " + textdf['APELLIDO'].str.capitalize()

    # Creamos la columba EDAD restando la fecha 25/11/1988
    textdf['NACIMIENTO'] = pd.to_datetime(textdf['NACIMIENTO'])
    textdf['AGE'] = pd.to_datetime ("25/11/1988", format= "%d/%m/%Y")

    textdf['EDAD [Años]'] = ((textdf['NACIMIENTO'] - textdf['AGE']).dt.days/365)

    #Hacemos left join entre textdf y grouped_excel_data
    outputdf = textdf.merge(grouped_excel_data, on='CEDULA', how='left')

    outputdf.to_csv(output_path, sep="|", index=False, quoting=csv.QUOTE_NONE, escapechar=" ")
    return


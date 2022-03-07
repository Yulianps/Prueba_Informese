# Importamos librerías necesarias en el main
import click

# Importamos funciones y procesos de los ejercicios
from src.ejercicio1.ejercicio1 import process_ejercicio1
from src.ejercicio2.ejercicio2 import process_ejercicio2
from src.ejercicio3.ejercicio3 import process_ejercicio3


# Ejemplo de como ejecutarlo:
# python.exe .\main.py --ejercicio=ejercicio1


# Definimos el job para el ejercicio1


def ejercicio1():
    
    input_path1 = 'inputs/ejercicio1_b1.xlsx'
    input_path2 = 'inputs/ejercicio1_b2.txt'
    output_path = 'outputs/ejercicio1/outputdf.csv'
    process_ejercicio1(input_path1, input_path2, output_path)

    return


# Definimos el job para el ejercicio2
def ejercicio2():
    
    input_path = 'inputs/ejercicio2_b1.json'
    process_ejercicio2(input_path)

    return


# Definimos el job para el ejercicio3
def ejercicio3():
    
    process_ejercicio3()
    
    return


# Creamos el click command para la ejecución de cada job de ejercicios
@click.command()
@click.option('--ejercicio', default='ejercicio1', help='Ingrese el ejercicio a resolver')

def main(ejercicio):
    
    if ejercicio == 'ejercicio1':
        ejercicio1()
    elif ejercicio == 'ejercicio2':
        ejercicio2()
    else:
        ejercicio3()
        
    return


if __name__ == "__main__":
    main()

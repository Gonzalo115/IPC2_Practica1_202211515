import os
from Tablero import Tablero
from ListaSimple import ListaSimple
from Pieza import Pieza

Juego = ListaSimple()


def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("INGRESAR UNA OPCCIÓN: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero o Opccion Valida')
    return num

def tablero():
    nombreT = 1
    fila = input("Ingrese el No. de Filas: ")
    columna = input("Ingrese el No. de Columnas: ")
    tablero = Tablero(nombreT, fila, columna)
    os.system('cls')
    salir2 = False
    opcion = 0
    while not salir2:
        print("")
        print("===========================================")
        print("        Practica 1 IPC2: Colorealo")
        print("===========================================")
        print("")
        print("1. Colocar Pieza")
        print("2. Salir y Generar Grafica")
        opcion = pedirNumeroEntero()

        if opcion == 1:
            os.system('cls')
            print("===========================================")
            print("        Practica 1 IPC2: Colorealo")
            print("              Agregar Pieza")
            print("===========================================")
            print("1. Azul")
            print("2. Rojo")
            print("3. Verde")
            print("4. Purpura")
            print("5. Naranja")

            color = input("Ingrese El Color Que Desea Agregar:")
            fila = input("Ingrese en que fila se desea agregar La pieza:")
            columna = input("Ingrese en que columna se desea agregar La pieza:")

            if color == "Azul":
                inicial = "A"
                nombre = "blue"

                pieza = Pieza(fila, columna, inicial, nombre)
                tablero.piezas.agregar_al_final(pieza)
                
            elif color == "Rojo":
                inicial = "R"
                nombre = "red"

                pieza = Pieza(fila, columna, inicial, nombre)
                tablero.piezas.agregar_al_final(pieza)
                
            elif color == "Verde":
                inicial = "V"
                nombre = "green"

                pieza = Pieza(fila, columna, inicial, nombre)
                tablero.piezas.agregar_al_final(pieza)
                
            elif color == "Purpura":
                inicial = "P"
                nombre = "purple"

                pieza = Pieza(fila, columna, inicial, nombre)
                tablero.piezas.agregar_al_final(pieza)
                
            elif color == "Naranja":
                inicial = "N"
                nombre = "orange"

                pieza = Pieza(fila, columna, inicial, nombre)
                tablero.piezas.agregar_al_final(pieza)
                
            else:
                print("La entrada no es una opcción.")
        
        elif opcion == 2:
            salir2 = True
        
        else: 
            print("Error")
        input("Presione ENTER para continuar...")
        os.system('cls')

    Juego.agregar_al_final(tablero)
    Juego.mostrar() 


def menu():
    salir = False
    opcion = 0
    while not salir:
        print("")
        print("===========================================")
        print("        Practica 1 IPC2:  Colorealo")
        print("===========================================")
        print("")
        print("1. Crear Tablero")
        print("2. Mostrar Datos Del Estudiante")
        print("3. Salir")
        opcion = pedirNumeroEntero()

        if opcion == 1:
            os.system('cls')
            print("")
            print("===========================================")
            print("        Practica 1 IPC2:  Colorealo")
            print("             Crear Tablero")
            print("===========================================")
            print("")
            tablero()

        elif opcion ==2:
            os.system('cls')
            print("")
            print("===========================================")
            print("        Practica 1 IPC2:  Colorealo")
            print("          Datos Del Estudiante")
            print("===========================================")
            print("")
            print("Nmbre:    Gonzalo Fernando Pérez Cazún")
            print("Carné:    202211515")
            print("Curso:    Introduccion a la Programcion y Computacion 2")
            print("Seccion:  A")
            print("Semestre: 4to Semestre")

        elif opcion == 3:
            salir = True
        else: 
            print("Error")
        input("Presione ENTER para continuar...")
        os.system('cls')


if __name__ == '__main__':
    menu()
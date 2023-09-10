import os

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

def menu():
    salir = False
    opcion = 0
    while not salir:
        print("")
        print("===========================================")
        print("  Practica 1 IPC2: Juego de Mesa “Colorealo”")
        print("===========================================")
        print("")
        print("1. Cargar Archivo")
        print("2. Mostrar Datos Del Estudiante")
        print("7. Salir")
        opcion = pedirNumeroEntero()

        if opcion == 1:
            print("Juego")
        elif opcion ==2:
            print("")
            print("===========================================")
            print("          Datos Del Estudiante")
            print("===========================================")
            print("")
            print("Nmbre:    Gonzalo Fernando Pérez Cazún")
            print("Carné:    202211515")
            print("Curso:    Introduccion a la Programcion y Computacion 2")
            print("Seccion:  A")
            print("Semestre: 4to Semestre")

        elif opcion == 7:
            salir = True
        else: 
            print("Error")
        input("Presione ENTER para continuar...")
        os.system('cls')


if __name__ == '__main__':
    menu()
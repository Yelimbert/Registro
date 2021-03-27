import os

nombreArchivo = "registro.txt"


def agregar():
    print("Ingrese los siguientes datos")

    nombre = input("Nombre: ")
    ape = input("Apellido: ")
    edad = input("Edad: ")
    cedula = input("Cedula: ")

    registro = nombre + ", " + ape + ", " + edad + ", " + cedula

    y = input("Desea guardar los datos/(si/no): ")
    if y == "si":
        with open(nombreArchivo, "a") as reg:
            datos = "\n" + registro
            reg.write(datos)


def header():
    reg = open(nombreArchivo, "w+")
    escribir = False
    primera_linea= "Nombre, Apellido, Edad, Cedula"
    if not os.path.isfile(nombreArchivo):
        escribir = True
    else:
        print(reg.read())
        escribir = len(reg.readlines()) == 0

    if escribir:
        reg.write(primera_linea)
        reg.close()

def buscar():
    with open(nombreArchivo, "r") as reg:
        texto = input("Por favor, inserta la cedula: ")
        for linea in reg.readlines():
            if linea.find(texto) > -1:
                print("Encontrado: " + linea)

def inicio():
    header()
    agregar()

    preg = input(
        "(y) Deseo ingresar mas datos\n(n) No deseo ingresar mas datos\n")

    if preg == "y":
        while preg == "y":
            agregar()
            preg = input(
                "(y) Deseo ingresar mas datos\n(n) No deseo ingresar mas datos: ")
            print(preg)
    elif preg == "n":
        print("No se almacenaran mas datos")
    interfaz()

def interfaz():
    print("Que desea realizar?")
    q = input("(1) Deseo ingresar datos\n(2) Deseo realizar una busqueda\n(3) No deseo hacer nada\n")
    if q == "1":
        inicio()
    elif q == "2":
        buscar()
    else:
        print("Ha salido del programa")

interfaz()

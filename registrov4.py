import os
import tempfile
import shutil
import getch
import sys

nombreArchivo = "registro.txt"
def name():
    nombre = ''
    print("Nombre: ")

    while True:
        ch = str(getch.getch())

        if ch == '\n': break
        
        if ch == '\x7f':
            nombre = nombre[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isalpha():
            nombre = nombre + ch

            sys.stdout.write("\r%s" % nombre)
            sys.stdout.flush()
    return nombre

def lastname():
    apellido = ''
    print("\nApellido: ")

    while True:
        ch = str(getch.getch())

        if ch == '\n': break

        if ch == '\x7f':
            apellido = apellido[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isalpha():
            apellido = apellido + ch

            sys.stdout.write("\r%s" % apellido)
            sys.stdout.flush()
    return apellido

def edad():
    edad = ''
    print("\nEdad: ")

    while True:
        ch = str(getch.getch())
        
        if ch == '\n': break

        if ch == '\x7f':
            edad = edad[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isnumeric():
            edad = edad + ch

            sys.stdout.write("\r%s" % edad)
            sys.stdout.flush()
    return edad

def identificacion():
    cedula = ''
    print("\nCedula: ")

    while True:
        ch = str(getch.getch())
        
        if ch == '\n': break

        if ch == '\x7f':
            cedula = cedula[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isnumeric():
            cedula = cedula + ch

            sys.stdout.write("\r%s" % cedula)
            sys.stdout.flush()
    return cedula

def account():
    monto = ""
    print("\nMonto: ")

    while True:
        ch = str(getch.getch())
        
        if ch == '\n': break

        if ch == '\x7f':
            monto = monto[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isdigit():
            monto = monto + ch

            sys.stdout.write("\rTu monto es de RD$ %s" % monto)
            sys.stdout.flush()
    return monto

def password():
    password = ''
    print("\nPassword: ")
    ast = ""

    while True:
        ch = getch.getch()

        if ch == '\n': break

        if ch == '\x7f':
            password = password[:-1]
            ast = ast[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isalnum():
            password = password + ch
            ast = ast + "*"

            sys.stdout.write("\r%s" % ast)
            sys.stdout.flush()
    return password

def confirm(password):
    passw = ""
    print('\nConfirmar password: ')
    ast = ""

    while True:
        ch = getch.getch()

        if ch == '\n': break

        if ch == '\x7f':
            password = password[:-1]
            ast = ast[:-1]
            
            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isalnum():
           passw = passw + ch
           ast = ast + "*"

           sys.stdout.write("\r%s" % ast)
           sys.stdout.flush()

    return passw == password

def obtenerDatos():
    print("Ingrese los siguientes datos")

    nombre = name()
    apellido = lastname()
    age = edad()
    cedula = identificacion()
    monto = account()
    return nombre + ", " + apellido + ", " + age + ", " + cedula + ", RD$ " + monto

def agregar():
    registro = obtenerDatos()
    passw = password()
    is_correct = confirm(passw)
    #y = input("\nDesea guardar los datos/(si/no): ")
    #if y == "si":
    if is_correct:
        with open(nombreArchivo, "a") as reg:
            datos = "\n" + registro
            reg.write(datos)
    else:
        print("Password don't match! No se guardaran los datos")

def header():
    escribir = False
    primera_linea= "Nombre, Apellido, Edad, Cedula, Monto"
    if not os.path.isfile(nombreArchivo):
        escribir = True
    else:
        with open(nombreArchivo, "r") as reg:
            check = reg.readlines()
            escribir = len(reg.readlines()) == 0

    if escribir == 0:
        with open(nombreArchivo, "w") as reg:
            reg.write(primera_linea)

def buscar():
    with open(nombreArchivo, "r") as reg:
        texto = input("Por favor, inserta la cedula: ")
        for linea in reg.readlines():
            if linea.find(texto) > -1:
                print("Encontrado: " + linea)
    main()

def mostrar():
    with open(nombreArchivo, "r") as reg:
        for line in reg.readlines():
            print(line)

    main()

def main():
    print("Que desea realizar?")
    q = input("(1) Deseo ingresar datos\n(2) Deseo ver que contiene el archivo\n(3) Deseo realizar una busqueda\n(4) Deseo editar datos\n(5) No deseo hacer nada\n")
    if q == "1":
        inicio()
    elif q == "2":
        mostrar()
    elif q == "3":
        buscar()
    elif q == "4":
        edit()

    else:
        print("Ha salido del programa")

def edit():
    edit = False
    delete = False
    tempreg, ruta_temp = tempfile.mkstemp()
    with open (tempreg, "w+") as new_reg:
        with open (nombreArchivo) as old_reg:
            pregunta = input("Que desea hacer?\n(1) Editar una linea\n(2) Eliminar una linea\n")
            if pregunta == "1":
                texto = input("Que datos quiere modificar?(Ingrese la cedula): ")
                for linea in old_reg.readlines():
                    print("Linea: '" + linea + "' - Search: '" + texto + "'")
                    if linea.find(texto) > -1:
                        datos = obtenerDatos()
                        new_reg.write("\n%s" % datos)
                        edit = True
                    else:
                        new_reg.write(linea)

            elif pregunta == "2":
                texto = input("Que datos desea eliminar?(Ingrese la cedula): ")
                for line in old_reg.readlines():
                    if line.find(texto) > -1:
                        line.strip(texto)
                        delete = True
                    else:
                        new_reg.write(line)
        
        if edit or delete:
            shutil.copymode(nombreArchivo, ruta_temp)
            os.remove(nombreArchivo)
            shutil.move(ruta_temp, nombreArchivo)


    main()


def inicio():
    header()
    agregar()

    preg = input("\n(y) Deseo ingresar mas datos\n(n) No deseo ingresar mas datos\n")

    if preg == "y":
        while preg == "y":
            agregar()
            preg = input("(y) Deseo ingresar mas datos\n(n) No deseo ingresar mas datos: ")
            print(preg)
    elif preg == "n":
        print("No se almacenaran mas datos")
    main()

main()

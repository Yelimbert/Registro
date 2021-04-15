import getch
import sys

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

def account():
    monto = ""
    print("\nIngrese un monto: ")

    while True:
        ch = str(getch.getch())
        
        if ch == '\n': break

        if ch == '\x7f':
            monto = monto[:-1]

            sys.stdout.write("\b \b")
            sys.stdout.flush()

        if ch.isnumeric():
            monto = monto + ch

            sys.stdout.write("\rTu monto es de RD$ %s" % monto)
            sys.stdout.flush()
    return monto

def main():
    nombre = name()
    apellido = lastname()
    age = edad()
    passw = password()
    is_correct = confirm(passw)
    

    if is_correct:
        print("\nSuccesfully!")
        account()
    elif is_correct == False:
        print("\nPasswords doesn't match!")
        confirm(passw)


main()



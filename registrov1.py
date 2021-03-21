import io

space = "\n"
datos = []
reg = open("registro.txt", "a")

dat = ("Nombre  Apellido  Edad  Cedula\n")
reg.write(dat)

print("Ingrese los siguientes datos")

name = input("Nombre: ")
datos.append(name)

ap = input("Apellido: ")
datos.append(ap)

age = input("Edad: ")
datos.append(age)

ced = input("Cedula: ")
datos.append(ced)
print(datos)

x = input("Desea grabar los datos? (si/no)")

if x == "si":
	for i in datos:
		i = i + ", "
		reg.write(i)
datos.append(space)

preg = input("(y) Deseo ingresar mas datos\n (n) No deseo ingresar mas datos\n")
print(preg)

if preg == "y":

	while preg == "y":

		datos.append(space)

		nombre = input("Nombre: ")
		datos.append(nombre)

		ape = input("Apellido: ")
		datos.append(ape)

		edad = input("Edad: ")
		datos.append(edad)

		cedula = input("Cedula: ")
		datos.append(cedula)

		y = input("Desea guardar los datos/(si/no): ")
		if y == "si":
			for i in datos:
				i = i + ", "
				reg.write(i)

		preg = input("(y) Deseo ingresar mas datos\n(n) No deseo ingresar mas datos: ")
		print(preg)

elif preg == "n":
	print("No se almacenaran mas datos")
	reg.close()
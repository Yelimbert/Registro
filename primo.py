def primo(h):
	n = h
	
	if n > 0:

		for i in range(2, n+1):
			c = 2
			primo = True

			while primo and c < i:
				if i % c == 0:
					primo = False

				else: 
					c += 1

			if primo:
				print(i, "es primo")
	else:
		print("El numero introducido no es valido")

x = lambda a : primo(a)
n = int(input("Ingrese un numero valor positivo: "))
print(x(n))
def SumRec(n):
    if n == 1:
        return 1
    else:
        return n + SumRec(n-1)

print(SumRec(10))

def NTSumRec(x):
    if x == 1:
        return 1
    else:
        x = x + NTSumRec(x-1)
        return x

print(NTSumRec(10))

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(5))

def NTfactorial(z):
	if z == 0:
		return 1
	else:
		z = z * factorial(z-1)
		return z

print(NTfactorial(5))

def mcd(n1, n2):
    if n1 > n2:
        if n1 % n2 == 0:
            return n2
        else:
            return mcd(n2, n1 % n2)
    else:
        return mcd(n2, n1)

print(mcd(20, 5))


def NTmcd(n, ni):
    if n > ni:
        if n % ni == 0:
            return ni
        else:
            m = mcd(ni, n % ni)
            return m
    else:
        x = mcd(ni, n)
        return x

print(NTmcd(8,7))

n = int(input("Ingrese el valor de n: "))
i = 1
sumatoria = 0

while i <= n:
    sumatoria += i
    i += 1
print(sumatoria)

def mcd(x, y):
    while(y):
        x, y = y, x % y
    return x
print(mcd(60, 48))

x = int(input("x: "))
count = 1
z = 1

while z <= x:
    count = count * z
    z = z + 1

print(count)
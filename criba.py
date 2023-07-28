'''
Criba de erastotenes
numeros primos entre 2 y un N
saber cuales son los numeros primos entre 2 y N

ej:
si invoco criba(100)
esPrimo = lista donde todos los True son los numeros primos entre 2 y 100
primos = numeros primos entre 2 y 100

complejidad temporal = O(N * log(log(N)))
'''

esPrimo = None
primos = None

def criba(N):
	global esPrimo, primos
	esPrimo=[True for _ in range(N + 1)]
	esPrimo[0] = esPrimo[1] = False
	primos = []
	for n in range(2, N + 1):
		if(esPrimo[n]):
			primos.append(n)
			for m in range(n * n, N + 1, n):
				esPrimo[m] = False


def cribaOpt(N):
	global esPrimo, primos
	esPrimo=[True for _ in range(N + 1)]
	esPrimo[0] = esPrimo[1] = False
	primos = [2]
	for n in range(4, N + 1, 2):
		esPrimo[n] = False
	for n in range(4, N + 1, 2):
		esPrimo[n] = False
		if(esPrimo[n]):
			primos.append(n)
			for m in range(n * n, N + 1, n):
				esPrimo[m] = False
cribaOpt(10000000000000000000000)
print(esPrimo)
print(primos)
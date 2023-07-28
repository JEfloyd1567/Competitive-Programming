esPrimo = None
primos = None
divs = None
facts = None
def criba(N):
	"""
	complejidad temporal = O(N * (log(log(N))))
	"""
	global esPrimo, primos, divs
	esPrimo = [True for _ in range(N + 1)]
	divs = [ i for i in range(N + 1)]
	esPrimo[0] = esPrimo[1] = False
	primos = [2]
	divs[2] = 2
	for n in range(4, N + 1, 2):
		esPrimo[n] = False
		divs[n] = 2
	for n in range(3, N + 1, 2):
		if(esPrimo[n]):
			primos.append(n)
			for m in range(n * n, N + 1, n):
				esPrimo[m] = False
				divs[m] = n

def descFacts(n):
	"""

	"""
	global facts
	facts = {}
	while(n != 1):
		d, c = divs[n], 0
		while( n % d == 0):
			c += 1
			n //= d
		facts[d] = c 
	return facts

criba(90000000)
descFacts(90000000)
print(esPrimo)
print(primos)
print(divs)
print(facts)
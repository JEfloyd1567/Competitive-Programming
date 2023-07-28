from sys import stdin, setrecursionlimit

setrecursionlimit(1 << 24)

T,P = None, None

def phi(n, m):
	"""
	complejidad temporal = O(2^n)
	complejidad espacial = O(1)
	"""
	ans = None
	if(m == 0):
		ans = 1
	elif(m > n):
		ans = 0
	elif(T[n - 1] == P[n - 1]):
		ans = phi(n - 1, m - 1) + phi(n - 1, m)
	else:
		ans = phi(n - 1, m)
	return ans

def phi_memo(n, m, mem):
	"""
	complejidad temporal = O(n * m)
	complejidad espacial = O(n * m)
	"""
	ans = None
	key = (n, m)
	if(key in mem):
		ans = mem[key]
	else:
		if(m == 0):
			ans = 1
		elif(m > n):
			ans = 0
		else:
			ans = phi_memo(n - 1, m, mem)
			if(T[n - 1] == P[m - 1]):
				ans += phi_memo(n - 1, m - 1, mem) 
	mem[key] = ans
	return ans

def phi_tab():
	N = len(T) 
	M = len(P)
	tab = [ [None for _ in range(M + 1)] for _ in range(N + 1) ]
	for n in range(N + 1):
		tab[n][0] = 1
	n = 0
	m = 1
	while(n != N + 1):
		if( m == M + 1):
			n,m = n + 1, 1
		else:
			if(m > n):
				tab[n][m] = 0
			else:
				tab[n][m] = tab[n-1][m]
			if(T[n-1] == P[m - 1]):
				tab[n][m] += tab[n-1][m-1]
		m += 1
	return tab[n][m]


def main():
	global T, P
	casos = int(stdin.readline())
	for i in range(casos):
		T = str(stdin.readline().strip())
		P = str(stdin.readline().strip())
		print(phi_memo(len(T), len(P), dict()))		
main()

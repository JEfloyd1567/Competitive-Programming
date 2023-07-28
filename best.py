from sys import stdin

def knapsack_memo(n, m, W, B, mem):
	"""
	O(N * M)
	"""
	if((n, m) in mem):
		ans = mem[(n, m)]
	else:
		if(n == 0 or m == 0):
			ans = 0
		elif(W[n - 1] <= m):
			ans = min(knapsack_memo(n - 1, m - W[n - 1], W, B, mem) + B[n - 1], knapsack_memo(n - 1, m, W, B, mem))
		else:
			ans = knapsack_memo(n - 1, m, W, B, mem)
		mem[(n, m)] = ans
	return ans

def main():
	n, x = map(int, stdin.readline().strip().split())
	while(n != 0 and x != 0):
		valores=[]
		valores.append(0)
		for i in range(n):
			p = stdin.readline().strip().split(".")
			pf = p[0] + p[1]
			pr = int(pf)
			valores.append(pr)
		print(knapsack_memo(valores[x], 5000, valores, valores, dict()))
		n, x = map(int, stdin.readline().strip().split())
main()
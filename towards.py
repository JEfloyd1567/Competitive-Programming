from sys import stdin

def rho(r, c):
	ans = None
	if(r >= N):
		ans = [c, c + 1]
	else:
		ans = list()
		if(c != 0):
			ans.append(c-1)
		if(c != r):
			ans.append(c)
	return ans 

def solve_aux(r, c, x, memo):
	ans, key = None, (r, c, x)
	if(key in memo):
		ans = memo[key]
	else:
		if(r == 0):
			ans = abs(board[0][0]) == abs(x)
		else:
			ans, n, NXT = False, 0, rho(r,c)
			while(ans == False and n != len(NXT)):
				ans = solve_aux(r - 1, NXT[n], x + board[r][c], memo) or solve_aux(r - 1, NXT[n], x - board[r][c], memo)
				n += 1
		memo[key] = ans
	return ans

def solve():
	ans, n, found, memo = None, 0, False, dict()
	while(found == False):
		found = solve_aux(rows - 1, 0, n, memo) or solve_aux(rows -1, 0, -n, memo)
		if(found):
			ans = n 
		n += 1
	return ans 

def main():
	global board, N, rows
	N = int(stdin.readline())
	while( N != 0):
		rows = (N << 1) - 1
		board = [list(map(abs, map(int, stdin.readline().split()))) for _ in range(rows)]
		print(solve())
		N = int(stdin.readline())

main()